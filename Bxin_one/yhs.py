import random
import turtle

__Pen = turtle.Pen()


# 分形樱花树

# “画树”函数
# 参数分别是树枝长度、画笔

def tree(branchLen, t):

    if (branchLen > 3):
        if (8 <= branchLen and branchLen <= 12):
            if (random.randint(0, 2) == 0):
                t.pencolor('snow')
            else:
                t.pencolor('lightcoral')
            t.pensize((branchLen / 3))
        elif (branchLen < 8):
            if (random.randint(0, 1) == 0):
                t.pencolor('snow')
            else:
                t.pencolor('lightcoral')
            t.pensize((branchLen / 2))
        else:
            t.pencolor('sienna')
            t.pensize((branchLen / 10))
        t.forward(branchLen)
        a = (1.5 * (random.random()))
        t.right((20 * a))
        b = (1.5 * (random.random()))
        # 在tree函数内部调自己，这种方式叫递归调用
        # 递归可以大幅提升编程效率
        tree(branchLen - 10 * b, t)
        t.left((40 * a))
        tree(branchLen - 10 * b, t)
        t.right((20 * a))
        t.penup()
        t.backward(branchLen)
        t.pendown()

# 绘制树下花瓣，参数分别是画板数、画笔

def petal(m, t):

    for i in range(m):
        a = (200 - 400 * (random.random()))
        b = (10 - 20 * (random.random()))
        t.penup()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.pendown()
        t.pencolor('lightcoral')
        t.circle(1)
        t.penup()
        t.backward(a)
        t.right(90)
        t.backward(b)

def main():

    t = turtle.Pen()
    __Pen.hideturtle()
    t.speed(0)
    turtle.bgcolor('wheat')
    t.left(90)
    t.penup()
    t.backward(150)
    t.pendown()
    t.pencolor('sienna')
    tree(60, t)
    petal(100, t)
    turtle.done()

main()