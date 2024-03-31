build:
	gfortran modify.f90 -o modify

run:
	./modify /Users/dhaffner/data/v8_climatology/OZON_CLIM.txt \
                 /Users/dhaffner/project/omi_to3_v85c4_alg1/data/final/SBUV_11_lyr_gmi_10deg.txt \
                 OZON_CLIM_GMI.txt

all: build run

clean:
	rm modify
