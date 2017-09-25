import sys

def main():
	board = init(int(sys.argv[1]))

	print("WELCOME TO GAME OF FIFTEEN\n")
	
	while True:
		display(board)
		inp = input("\nTile to move:")
		try:
			move = int(inp)
		except:
			pass
		slide(board, move)
		if check(board):
			break
		print("\033[2J")
	print("\033[2J")
	print("Yay You Win!")

def slide(b, m):
	move = [0, 0]
	zero = [0, 0]
	for y in range(len(b)):
		for x in range(len(b[y])):
			if m == b[y][x]:
				move = [x, y]
			elif 0 == b[y][x]:
				zero = [x, y]
	if (abs(move[0] - zero[0]) == 1 and move[1] == zero[1]) or (abs(move[1] - 
zero[1]) == 1 and move[0] == zero[0]):
		b[move[1]][move[0]], b[zero[1]][zero[0]] = b[zero[1]][zero[0]], b[move[1]][move[0]]

def check(b):
	won = True
	for i in range(len(b)**2):
		if b[i//len(b)][i%len(b)] != i:
			won = False
			break
	return won

def init(n):
	board = []
	for i in range(n**2 - 1, -1, -1):
		if (i+1)%n == 0:
			board.append([])
		board[(n**2 - i - 1)//n].append(i)
	if n%2 == 0:
		board[-1][-2], board[-1][-3] = board[-1][-3], board[-1][-2]
	return board

def display(b):
	for r in b:
		for c in r:
			print(c, end="\t")
		print()

if __name__ == "__main__":
	main()
