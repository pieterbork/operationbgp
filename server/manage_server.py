import sys


def kill_server(color):
    f = open('colors.txt', 'r')
    colors = f.readline().strip().split(',')
    colors.remove(color)
    f.close()
    f = open('colors.txt', 'w')
    writeline = ",".join(colors).strip()
    f.write(writeline)
    f.close()

def add_server(color):
    f = open('colors.txt', 'r')
    colors = f.readline().strip().split(',')
    f.close()
    if color in colors:
        print("server is already alive!")
    else:
        f = open('colors.txt', 'w')
        colors.append(color)
        writeline = ",".join(colors).strip()
        f.write(writeline)
        f.close()

def main():
    args = sys.argv

    if len(args) < 3:
        print("not enough args")
        quit()

    op = args[1]
    num = int(args[2])

    colors = ["red", "green", "blue"]

    try:
        color = colors[num]
    except:
        print("server not found!")

    if op == "kill":
        kill_server(color)
    elif op == "add":
        add_server(color)

main()
