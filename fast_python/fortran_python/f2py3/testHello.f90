        program hello
                external printhello
                real :: A=1.
                call printhello(A)
        end program hello
        
        subroutine printhello(A)
                real :: A
                print *, "Hello World!"
                return
        end
