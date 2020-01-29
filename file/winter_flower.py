import time
import turtle

times = time.perf_counter()


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    global times
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 4  # 这是是科赫曲线的数量
    koch(400, level)
    turtle.rt(120)
    koch(400, level)
    turtle.rt(120)
    koch(400, level)
    turtle.hideturtle()
    print("画图所用时间时间{}秒!".format(time.perf_counter() - times))
    turtle.done()


main()

print("程序运行时间{}秒!".format(time.perf_counter() - times))
input('按Enter关闭窗口！！！')
