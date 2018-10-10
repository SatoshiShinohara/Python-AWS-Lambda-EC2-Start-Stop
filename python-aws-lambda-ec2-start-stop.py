import boto3

def lambda_handler(event, context):
    # リージョンを取得
    client = boto3.client('ec2', event['Region'])

    # リージョン内のインスタンスID一覧と起動・停止対象のインスタンスIDを取得
    responce = client.describe_instances()
    all_list = []
    no_list = []
    for reservation in responce['Reservations']:
        for instance in reservation['Instances']:
            # 全インスタンスIDをリストに追加
            all_list.append(instance['InstanceId'])

            # 起動・停止対象外のインスタンスIDをリストに追加
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == event['Tag'] and tag['Value'] == event['Value']:
                        no_list.append(instance['InstanceId'])

    # 全インスタンスリストと起動・停止対象外のインスタンスとの差分を取得
    diffset = set(all_list) - set(no_list)

    # 起動・停止対象のインスタンスID一覧を取得
    target_list = list(diffset)

    # 起動・停止を実行
    if event['Action'] == 'start':
        client.start_instances(InstanceIds=target_list)
    elif event['Action'] == 'stop':
        client.stop_instances(InstanceIds=target_list)
