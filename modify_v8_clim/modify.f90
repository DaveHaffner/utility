! replace layer zero total ozone in V8 climatology with values from
! GMI in SBUV climatology
program reformat
  implicit none
  integer(kind=4) :: k, j, i, month, ios
  real(kind=4) :: lat, toz
  real(kind=4), dimension(11) :: prf, prf_gmi
  character(len=256) :: filename, filename2, filename3, tmp_str
  call get_command_argument(1, filename)
  call get_command_argument(2, filename2)
  call get_command_argument(3, filename3)
  open(22, status='old', file= trim(filename))
  open(24, status='old', file= trim(filename2))
  open(23, status='unknown', file=trim(filename3))

  write(*,*) trim(filename)
  write(*,*) trim(filename2)
  write(*,*) trim(filename3)
  
  do k = 1, 12
     read( 24, "(6x,i2)", iostat = ios) month
     do j = 1, 18
        read( 22, "(9x,i2,12x,f6.1)", iostat = ios) month, lat
        write( 23, "(a9,i2,a12,f6.1)", iostat = ios) "Month = ", month, "Latitude = ", lat
        read( 24, "(f5.1,1X,10(f6.2,1X),f6.2)", iostat = ios) lat, prf_gmi
        do i = 1, 10
           read( 22, "(1x,f6.1,6f7.2,5f6.2)", iostat = ios) toz, prf
           if (prf(1) == 999.00) then
              continue
           else
              prf(1) = prf_gmi(1)
           endif
           write( 23, "(1x,f6.1,6f7.2,5f6.2)", iostat = ios) toz, prf
        enddo
     enddo
  enddo
!  close(23)
  close(22)
end program reformat
