import argparse
import sys
# def calc(args):
#     if args.o == "add":
#         return args.x + args.y
#     elif args.o == "sub":
#         return args.x - args.y
#     elif args.o == "mul":
#         return args.x * args.y
#     elif args.o == "div":
#         return args.x/args.y
#     else:
#         return "something went worng"
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,
#                                 help = "Enter first number")
#
#     parser.add_argument('--y', type = float, default=3.0,
#                         help="Enter second number")
#
#     parser.add_argument('--o', type = str, default="add",
#                         help="Enter utility for calculation")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))

def calc(args):
    if args.o == 'add':
        if args.x==56 and args.y==9:
            print("77")
        else:
            return args.x+ args.y
    elif args.o == 'mul':
        if args.x==45 and args.y==3:
            print("555")
        else:
            return args.x*args.y
    elif args.o == 'div':
        if args.x==56 and args.y==6:
            print("4")
        else:
            return args.x/args.y
    elif args.o == 'sub':
        return args.x-args.y
    else:
        return "Incorrect keywords"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                                help = "Enter first number")

    parser.add_argument('--y', type = float, default=3.0,
                        help="Enter second number")

    parser.add_argument('--o', type = str, default="add",
                        help="Enter utility for calculation")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))