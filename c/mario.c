#include <stdio.h> /* fprintf */
#include <unistd.h> /* getopt */
#include <string.h>

int main(int argc, char *argv[]){
    char **positionals;
    positionals = &argv[optind];

    if (argc != 2) {
        printf("Missing arguments\n");
        return 1;
    }

    for (; *positionals; positionals++)
        fprintf(stdout, "Positional: %s\n", *positionals);
    return 0;
}