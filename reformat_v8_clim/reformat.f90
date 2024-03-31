program reformat
  implicit none
  integer(kind=4) :: k, j, i, month
  integer(kind=4) :: ios
  real(kind=4) :: lat, toz
  real(kind=4), dimension(11) :: prf
  character(len=256) :: filename
  call get_command_argument(1, filename)
  open(22, file= trim(filename))
  open(23, file="v8_clim.txt")
  do k = 1, 12
     do j = 1, 18
        read( 22, "(9x,i2,12x,f6.1)", iostat = ios) month, lat
        do i = 1, 10
           read( 22, "(1x,f6.1,6f7.2,5f6.2)", iostat = ios) toz, prf
           write(23,'(i2, 1x, f6.2, 1x, f6.2, 11f7.2)') month, lat, toz, prf
        enddo
     enddo
  enddo
  close(23)
  close(22)
end program reformat
