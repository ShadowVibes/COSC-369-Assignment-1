#include <stdio.h>
#include "formatter.h"

int main(void)
{
    const char *input_file = "Combined_Schedule_Office_Hours.txt";
    const char *output_file = "formatted_schedule.txt";

    printf("Formatting class schedule and office hours...\n");

    if (format_schedule(input_file, output_file) != 0)
    {
        printf("Formatting failed.\n");
        return 1;
    }

    printf("Output written to %s\n", output_file);

    return 0;
}