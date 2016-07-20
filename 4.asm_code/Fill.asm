// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.


// clear the screen
(CLEAR)
	// i variable for loop
	// screen memory starts at RAM address 16384
	@16384
	D=A
	@i
	M=D
	(CLEAR_LOOP)
		// clear the screen at i memory address
		@0
		D=A
		@i
		A=M
		M=D

		// increase i
		@i
		M=M+1

		// keyboard RAM address 24576
		@24576
		D=M
		// if no key is pressed continue looping
		// else go to BLACKEN
		@CLEAR_LOOP
		D,JEQ


// blacken the screen
(BLACKEN)
	// i variable for loop
	// screen memory starts at RAM address 16384
	@16384
	D=A
	@i
	M=D
	(BLACKEN_LOOP)
		// blacken the screen at i memory address
		@1
		D=-A
		@i
		A=M
		M=D

		// increase i
		@i
		M=M+1

		// keyboard RAM address 24576
		@24576
		D=M
		// if a key is pressed continue looping
		// else go to CLEAR
		@BLACKEN_LOOP
		D,JNE
		@CLEAR
		D,JEQ
