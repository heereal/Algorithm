n = int(input())
heart = [' @@@   @@@ ', '@   @ @   @', '@    @    @', '@         @', ' @       @ ', '  @     @  ', '   @   @   ', '    @ @    ', '     @     ']

for line in heart:
    print((line + " ")* n)