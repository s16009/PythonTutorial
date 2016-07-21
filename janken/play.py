HANDS = ('グー', 'チョキ', 'パー')


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """
    import random
    return random.choice(HANDS)


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1、あいこは０、負けは−1を返す
    """
    if player == 1:
        if computer == 'チョキ':
            return 1
        elif compter == 'パー':
            return -1
        else:
            return 0

    elif player == 2:
        if compter == 'パー':
            return 1
        elif compter == 'グー':
            return -1
        else:
            return 0

    elif player == 3:
        if compter == 'グー':
            return 1
        elif computer == 'チョキ':
            return -1
        else:
            return 0


def save_score(result):
    """
    'score.txt'に戦績を保存
    win:x lose:y draw:zのディクショナリデータを保存する
    :param result:
    :return:
    """
    import json
    dic = {"win": "x"}
    dic2 = {"lose": "y"}
    dic3 = {"draw": "z"}

    with open('score.txt', 'a') as f:
        if result == 1:
            json.dump(dic, f, sort_keys=True, indent=4)
        elif result == -1:
            json.dump(dic2, f, sort_keys=True, indent=4)
        elif result == 0:
            json.dump(dic3, f, sort_keys=True, indent=4)
    return None


if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    compter = select_hand()
    result = judgement(player, compter)
    # コンピュータの手と勝敗の結果を表示
    print(compter)

    if result == 1:
        print("win")
    elif result == 0:
        print("draw")
    elif result == -1:
        print("lose")

    save_score(result)
