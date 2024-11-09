dna_sequences = open("dna.txt").read().lower().split("\n")
def AT_content(dna: str):
        return (dna.count("a") + dna.count("t")) / len(dna) * 100
at_sequences = list(map(AT_content, dna_sequences.copy()))
print("AT content analysis: ")
for i in range(len(dna_sequences)):
    print(f"{dna_sequences[i][:10]}...: {at_sequences[i]:.2f}")
