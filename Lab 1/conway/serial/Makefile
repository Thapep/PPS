all: omp_game_of_life

omp_game_of_life: Game_Of_Life.c

	gcc -O3 -fopenmp -o omp_gol Game_Of_Life.c

clean:
	rm omp_gol mgol.err mgol.out rgol.err rgol.out
