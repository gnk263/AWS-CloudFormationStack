import boto3

cfn = boto3.client('cloudformation')


def main():
    # スタック一覧を取得する
    stacks = get_stacks()

    # 各スタックのリソース数を調べる
    result = []
    for stack in stacks:
        stack_name = stack['StackName']
        resources = get_stack_resources(stack_name)
        result.append({
            'StackName': stack_name,
            'ResourceCount': len(resources)
        })

    # 結果を表示する
    display(stacks, result)


def get_stacks(token=None):
    option = {
        'StackStatusFilter': ['CREATE_COMPLETE']
    }

    if token is not None:
        option['NextToken'] = token

    res = cfn.list_stacks(**option)
    stacks = res.get('StackSummaries', [])

    if 'NextToken' in res:
        stacks += get_stacks(res['NextToken'])
    return stacks


def get_stack_resources(stack_name, token=None):
    option = {
        'StackName': stack_name
    }

    if token is not None:
        option['NextToken'] = token

    res = cfn.list_stack_resources(**option)
    resources = res.get('StackResourceSummaries', [])

    if 'NextToken' in res:
        resources += get_stack_resources(res['NextToken'])
    return resources


def display(stacks, result):
    # リソース数が多い順に表示する
    for item in sorted(result, key=lambda x:x['ResourceCount'], reverse=True):
        stack_name = item['StackName']
        resource_count = item['ResourceCount']
        print(f'{stack_name}({resource_count})')

    print('----------------------------')
    print(f'total stack: {len(stacks)}')


if __name__ == "__main__":
    main()
