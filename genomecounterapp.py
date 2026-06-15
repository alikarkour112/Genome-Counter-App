import streamlit as st

# Set the title and description of the website
st.title("🧬 Genome Sequence Analyzer")
st.write("Enter your DNA/Genome sequence below to calculate the total nucleotides and count each nitrogenous base.")

# Create a text input area for the user
user_input = st.text_area("Paste your Genome Sequence here:", "ATCGATCGATCGATCGAATTCG")
gc_threshold = 45.0
# Clean and process the input
genome_sequence = user_input.strip().upper()

# Verification: Ensure the sequence only contains valid characters
valid_bases = set("ATCG")
if any(base not in valid_bases for base in genome_sequence if base.strip()):
    st.warning("⚠️ Warning: Your sequence contains characters other than A, T, C, or G. Please check your input.")

sequence_length = len(genome_sequence)

# Calculate results
total_nucleotides = len(genome_sequence)
count_A = genome_sequence.count("A")
count_T = genome_sequence.count("T")
count_C = genome_sequence.count("C")
count_G = genome_sequence.count("G")

g_count = genome_sequence.count('G')
c_count = genome_sequence.count('C')

# Calculate the total GC percentage
gc_content = ((g_count + c_count) / sequence_length) * 100

# Check if the GC content meets the threshold
is_high_gc = gc_content > gc_threshold
# Display the results in a nice UI layout
st.subheader("📊 Analysis Results")

# Display total count
st.metric(label="Total Nucleotides", value=total_nucleotides)

# Display individual counts in columns
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Adenine (A)", value=count_A)
with col2:
    st.metric(label="Thymine (T)", value=count_T)
with col3:
    st.metric(label="Cytosine (C)", value=count_C)
with col4:
    st.metric(label="Guanine (G)", value=count_G)
    
# --- NEW CODE ADDED BELOW ---

st.markdown("---")
st.subheader("🧪 GC Content Analysis")

# Display the GC percentage formatted to 2 decimal places
st.metric(label="GC Content Percentage", value=f"{gc_content:.2f} %")

# Display an interactive alert based on the threshold
if is_high_gc:
    st.success(f"Yes, GC Content is ABOVE the threshold ({gc_threshold}%)! 🎉")
else:
    st.info(f"No, GC Content is BELOW the threshold ({gc_threshold}%).")