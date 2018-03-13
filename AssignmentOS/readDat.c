#include <stdio.h>

void read_in_dat (const char*);

void read_in_dat (const char* file_name) {
      FILE* file = fopen (file_name, "r");
      int i = 0;

      fscanf (file, "%d", &i);
      while (!feof (file)) {
            printf("%d ", i * i);
            fscanf (file, "%d", &i);
      }
      fclose (file);
      printf("\n");
}
