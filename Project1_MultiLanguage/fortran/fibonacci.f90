! fibonacci.f90
! Program to generate the first N Fibonacci numbers

program fibonacci_creator
    implicit none
    integer :: N, i                ! N = number of terms, i = loop counter
    integer, allocatable :: fib(:) ! dynamic array to hold Fibonacci numbers

    ! Ask user for input
    print *, "Enter the number of Fibonacci terms to generate (N):"
    read *, N

    ! Check input validity
    if (N <= 0) then
        print *, "Error: Please enter a positive integer."
        stop
    end if

    ! Allocate array of size N
    allocate(fib(N))

    ! Base cases of Fibonacci sequence
if (N >= 1) fib(1) = 1
    if (N >= 2) fib(2) = 1

    ! Compute sequence using iteration
    do i = 3, N
        fib(i) = fib(i-1) + fib(i-2)
    end do

    ! Print header 
    print "(A,I0,A)", "First ", N, " Fibonacci numbers:"

    ! Print output in one line
    print "(100(I0,1X))", fib  ! up to 100 integers, separated by spaces

    ! Free allocated memory
    deallocate(fib)

end program fibonacci_creator