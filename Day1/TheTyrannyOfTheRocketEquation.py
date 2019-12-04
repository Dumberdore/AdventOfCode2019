try:
	fp = open('input.txt')
	totalFuelRequired = 0
	for cnt, line in enumerate(fp):
		if int(line) > 3:
			currFuelRequired = (int(line) // 3) - 2
		else:
			currFuelRequired = 0

		print(currFuelRequired)
		totalFuelRequired += currFuelRequired

	print(totalFuelRequired)
finally:
	fp.close()