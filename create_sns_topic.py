import yaml


def main():

    for i in range(196):
        topic = {
            f'ResourceTestSnsTopic{i+1:03}': {
                'Type': 'AWS::SNS::Topic',
                'Properties': {
                    'TopicName': f'resource-test-sns-topic-{i+1:03}'
                }
            }
        }
        ym = yaml.dump(topic)
        print(ym)

if __name__ == "__main__":
    main()
