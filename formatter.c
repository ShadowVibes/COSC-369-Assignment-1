#include <stdio.h>
#include <string.h>
#include "formatter.h"

int format_schedule(const char *input_file, const char *output_file)
{
    FILE *input = fopen(input_file, "r");

    if (input == NULL)
    {
        printf("Error opening input file.\n");
        return 1;
    }

    FILE *output = fopen(output_file, "w");

    if (output == NULL)
    {
        printf("Error creating output file.\n");
        fclose(input);
        return 1;
    }

    char line[500];
    int office_hours_started = 0;

    fprintf(output, "CLASS SCHEDULE\n");
    fprintf(output, "==================================================\n\n");

    while (fgets(line, sizeof(line), input))
    {
        if (strstr(line, "Combined Class Schedule") != NULL)
        {
            continue;
        }

        if (strstr(line, "==================================================") != NULL)
        {
            continue;
        }

        if (strncmp(line, "Office Hours:", 13) == 0)
        {
            if (!office_hours_started)
            {
                fprintf(output, "\nOFFICE HOURS\n");
                fprintf(output,
                        "NOTE: Instructors are not to be interrupted during class times.\n\n");

                office_hours_started = 1;
            }

            char *hours = line + 13;

            while (*hours == ' ' || *hours == '\t')
            {
                hours++;
            }

            if (strncmp(hours, "Office Hours:", 13) == 0)
            {
                hours += 13;

                while (*hours == ' ' || *hours == '\t')
                {
                    hours++;
                }
            }

            fprintf(output, "Office Hours: %s", hours);
            continue;
        }

        if (strstr(line, ": nan") != NULL)
        {
            char *colon = strchr(line, ':');

            if (colon != NULL)
            {
                int length = (int)(colon - line);
                fprintf(output, "%.*s: N/A\n", length, line);
            }

            continue;
        }

        fprintf(output, "%s", line);
    }

    fclose(input);
    fclose(output);

    printf("Formatted schedule created successfully.\n");

    return 0;
}