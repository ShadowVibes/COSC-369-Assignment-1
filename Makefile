CC = gcc
AR = ar
CFLAGS = -Wall -Wextra

TARGET = schedule_formatter.exe
LIBRARY = libformatter.a
OBJECT = formatter.o

.PHONY: all final run clean update_schedule

all: final

$(OBJECT): formatter.c formatter.h
	$(CC) $(CFLAGS) -c formatter.c -o $(OBJECT)

$(LIBRARY): $(OBJECT)
	$(AR) rcs $(LIBRARY) $(OBJECT)

$(TARGET): main.c formatter.h $(LIBRARY)
	$(CC) $(CFLAGS) main.c $(LIBRARY) -o $(TARGET)

update_schedule:
	python main.py

formatted_schedule.txt: $(TARGET) update_schedule
	./$(TARGET)

Final_Schedule.docx: formatted_schedule.txt generate_word.py
	python generate_word.py

final: Final_Schedule.docx
	@echo "Final schedule generated successfully."

run: final

clean:
	rm -f $(OBJECT) $(LIBRARY) $(TARGET) Combined_Schedule_Office_Hours.txt formatted_schedule.txt Final_Schedule.docx