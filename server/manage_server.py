import sys


def kill_server(color):
    f = open('colors.txt', 'r')
    colors = f.readline().split(',')
    if color in colors:
        colors.remove(color)
        f.close()
        f = open('colors.txt', 'w')
        writeline = ",".join(colors)
        print(writeline)
        f.write(writeline)
        f.close()
    else:
        print("server is not alive!")

def add_server(color):
    f = open('colors.txt', 'r')
    colors = f.readline().split(',')
    f.close()
    if color in colors:
        print("server is already alive!")
    else:
        f = open('colors.txt', 'w')
        colors.append(color)
        writeline = ",".join(colors)
        f.write(writeline)
        f.close()

def main():
    args = sys.argv

    if len(args) < 3:
        print("not enough args")
        quit()

    op = args[1]
    num = int(args[2])
    print(op, num)

    colors = ["red", "green", "blue"]

    if op == "kill":
        kill_server(colors[num])
    elif op == "add":
        add_server(colors[num])

main()
