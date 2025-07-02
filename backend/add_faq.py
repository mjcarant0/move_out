from backend_faq import insert_faq

print("🛠 FAQ Entry Tool")
print("Type your new FAQ below. Press Enter to submit.\n")

while True:
    question = input("🟡 Question (or type 'exit' to stop): ").strip()
    if question.lower() == "exit":
        break

    answer_lines = []
    print("🟢 Type your answer line-by-line. Type 'done' to finish:")
    while True:
        line = input("  > ").strip()
        if line.lower() == "done":
            break
        answer_lines.append(line)

    answer = "\n".join(answer_lines)

    insert_faq(question, answer)
    print("✅ FAQ added successfully!\n")
