// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// input of R0
@2
D=A
@R0
M=D

// input of R1
@4
D=A
@R1
M=D

// clean R2
@0
D=A
@R2
M=D

// i variable for loop
@1
D=A
@i
M=D

(LOOP_R0_TIMES)
	@R1
	D=M
	@R2
	M=M+D
	@i
	M=M+1
	D=M
	@R0
	D=M-D
	@LOOP_R0_TIMES
	D,JGE

// end program
(END)
@END
0,JMP