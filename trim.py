import cv2
import numpy as np
import os


class mouseParam:
    def __init__(self, input_img_name):
        # マウス入力用のパラメータ
        self.mouseEvent = {"x": None, "y": None, "event": None, "flags": None}
        # マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)

    # コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags

        # マウス入力用のパラメータを返すための関数

    def getData(self):
        return self.mouseEvent

    # マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]

        # マウスフラグを返す関数

    def getFlags(self):
        return self.mouseEvent["flags"]

        # xの座標を返す関数

    def getX(self):
        return self.mouseEvent["x"]

        # yの座標を返す関数

    def getY(self):
        return self.mouseEvent["y"]

        # xとyの座標を返す関数

    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])


def cnt():
    f_path = "filtered"
    r_path = "raw"

    f_files = os.listdir(f_path)
    r_files = os.listdir(r_path)

    f_cnt = len(f_files)
    r_cnt = len(r_files)

    if f_cnt == r_cnt:
        return f_cnt
    else:
        print("データセットの数が合いません")


# アフィン変換
def affine(x, y):
    matrix1 = np.array([[3, 0, 0], [0, 3, 0], [0, 0, 1]])
    matrix2 = np.array([[x], [y], [1]])

    matrix3 = matrix1.dot(matrix2)

    return int(matrix3[0]), int(matrix3[1])


if __name__ == "__main__":
    # 画像の数を数える
    num = cnt()

    for i in range(num):

        n = 1

        # 入力画像 4608x3456
        filtered = cv2.imread("filtered/" + str(i + 1) + ".jpg")
        raw = cv2.imread("raw/" + str(i + 1) + ".jpg")
        # リサイズ 1/3
        f_resized = cv2.resize(filtered, (1536, 1152))
        r_resized = cv2.resize(raw, (1536, 1152))

        # 表示するWindow名
        window_name = "filtered"+ str(i+1)
        raw_window = "raw" + str(i + 1)

        # 画像の表示
        cv2.imshow(window_name, f_resized)
        cv2.imshow(raw_window, r_resized)

        mouseData = mouseParam(window_name)
        pos1x = 0
        pos1y = 0
        pos2x = 0
        pos2y = 0

        while 1:
            cv2.waitKey(20)
            # 左クリックがあったら表示
            if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
                if n == 1:
                    pos1x, pos1y = mouseData.getPos()
                    print("first" + str(pos1x) + ":" + str(pos1y) + ", " + str(pos2x) + ":" + str(pos2y))
                    n = 2
                elif n == 2:
                    pos2x, pos2y = mouseData.getPos()
                    print("second" + str(pos1x) + ":" + str(pos1y) + ", " + str(pos2x) + ":" + str(pos2y))
                print(mouseData.getPos())
            # 右クリックがあったら終了
            elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
                break

        print("out" + str(pos1x) + ":" + str(pos1y) + ", " + str(pos2x) + ":" + str(pos2y))

        # 4608x3456の座標にアフィン変換
        pos1x, pos1y = affine(pos1x, pos1y)
        pos2x, pos2y = affine(pos2x, pos2y)
        print("affine→" + str(pos1x) + ":" + str(pos1y) + ", " + str(pos2x) + ":" + str(pos2y))

        # 切り取った不明な寸法の画像の中心を取得
        centerx = int(0.5 * (pos1x + pos2x))
        centery = int(0.5 * (pos1y + pos2y))

        # 256x256サイズで切り出し
        f_trimed = filtered[centery - 128: centery + 128, centerx - 128: centerx + 128, :]
        r_trimed = raw[centery - 128: centery + 128, centerx - 128: centerx + 128, :]

        cv2.imwrite("trimed/filtered/f" + str(i + 1) + ".jpg", f_trimed)
        cv2.imwrite("trimed/raw/r" + str(i + 1) + ".jpg", r_trimed)

        print("f" + str(i+1) + "done")
        cv2.destroyAllWindows()

    print("Finished")
