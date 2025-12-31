; fib.ll
; Calculate fib(n) where n is read from command line as argv[1]
; Returns fib(n)

declare i32 @atoi(i8*) ;Tried to do with with int but kept getting an error that this fixed, from stack overflow using i8* instead of i32* 
    ;makes it a string which command lines uses on raw input(for my windows machine at least)

define i32 @main(i32 %argc, i8** %argv) {
entry:
  ; Load argv[1]
  %arg1_ptr = getelementptr inbounds i8*, i8** %argv, i32 1
  %arg1 = load i8*, i8** %arg1_ptr

  ; Convert string to int by doing n = atoi(argv[1]) after getting the input had to change it back to an int to use the rest of our functions
  %n = call i32 @atoi(i8* %arg1)

  ; Check: if n == 0, first base case of our comparisons
  %cmp0 = icmp eq i32 %n, 0
  br i1 %cmp0, label %ret0, label %check1

ret0:
  ret i32 0

check1:
  ; Check: if n == 1
  %cmp1 = icmp eq i32 %n, 1
  br i1 %cmp1, label %ret1, label %loop

ret1:
  ret i32 1

;Loop starts here to compute fib(n), I really like how labeled things get in this and can see how we can easily translate this into different comparison methods
loop:
  br label %loop_header

loop_header:
  ; PHI nodes: set up loop variables
  %i = phi i32 [2, %loop], [%i_next, %loop_body]
  %a = phi i32 [0, %loop], [%b, %loop_body]
  %b = phi i32 [1, %loop], [%sum, %loop_body]

  ; Break when i > n
  %cmp = icmp sgt i32 %i, %n
  br i1 %cmp, label %return, label %loop_body

loop_body:
  ; sum = a + b
  %sum = add i32 %a, %b
  ; i_next = i + 1
  %i_next = add i32 %i, 1
  br label %loop_header

return:
  ret i32 %b
}
