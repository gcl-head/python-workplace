import win32gui

from PIL import ImageGrab
from PIL import ImageChops


class gh:
    hwndTitle = {}

    def get_all_hwnd(self, hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) \
                and win32gui.IsWindowVisible(hwnd) and win32gui.IsIconic(hwnd) == 0:
            self.hwndTitle[hwnd] = win32gui.GetWindowText(hwnd)

    def getallhwnds(self):
        win32gui.EnumWindows(self.get_all_hwnd, 0)
        return self.hwndTitle.items()


if __name__ == '__main__':
    hwnd_title = gh().getallhwnds()
    print(hwnd_title)
    if hwnd_title is not None:
        hwnd = None
        for i, j in hwnd_title:
            if "大家来找茬" in j and "辅助" not in j:
                # print(i, j)
                hwnd = i
                break
        if hwnd is not None:
            tua = win32gui.GetWindowRect(hwnd)

            t1 = [tua[0] + 93, tua[1] + 312, tua[2] - 550, tua[3] - 170]
            t2 = [tua[2] - 474, tua[1] + 312, tua[2] - 93, tua[3] - 170]

            im1 = ImageGrab.grab(t1)
            im2 = ImageGrab.grab(t2)

            diff = ImageChops.difference(im1, im2)

            diff.show()
        else:
            print("未发现非最小化游戏窗口")
    else:
        print("未发现非最小化窗口")
