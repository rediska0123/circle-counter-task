import circle_counter
import sys


def main():
	if len(sys.argv) != 2:
		print('usage: python3 main.py filename')
		sys.exit(1)
	filename = sys.argv[1]
	(red, black) = circle_counter.count_circles(filename)
	
	print("Read circles:", red)
	print("Black circles:", black)


if __name__ == '__main__':
	main()
