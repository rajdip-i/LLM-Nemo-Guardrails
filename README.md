# Local LLM Guardrails Lab

A experimentation project for building, testing, and refining
conversational guardrails with [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) and [Ollama](https://ollama.com/)

- topical boundaries for a task-focused assistant;
- basic jailbreak detection and refusal flows;
- fact-constrained answers from a small knowledge base; and
- controlled execution of custom actions.


## Stack

| Component | Purpose |
| --- | --- |
| NeMo Guardrails | Conversation orchestration and Colang rails |
| Ollama | Local model server |
| `llama3.2` | Default local LLM |

Every experiment uses Ollama's default OpenAI-compatible endpoint:
`http://localhost:11434/v1`.

## Experiments

| Script | What it explores | Configuration |
| --- | --- | --- |
| `topical.py` | Routes politics and financial-advice requests to fixed refusals while allowing recipe questions. | `config_topical/` |
| `jailbreak.py` | Tests defined jailbreak patterns alongside a normal request. | `config_jailbreak/` |
| `fact_checking.py` | Constrains responses to the facts in the configuration. | `config_fact_checking/` |
| `actions.py` | Invokes custom Python actions for the current time, date, and demonstration weather. | `config_actions/` |

## Quick start

### 1. Prepare Ollama

Install Ollama, then download the model:

```bash
ollama pull llama3.2
```

Ensure the local server is running. The desktop application normally starts it
automatically; otherwise run:

```bash
ollama serve
```

Confirm that Ollama can see the model:

```bash
ollama list
```

### 2. Create a Python environment

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 3. Run an experiment

```bash
python3 jailbreak.py
```

Run the other experiments independently:

```bash
python3 topical.py
python3 fact_checking.py
python3 actions.py
```


- [NeMo Guardrails documentation](https://docs.nvidia.com/nemo/guardrails/)
- [NeMo Guardrails model configuration](https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/yaml-schema/model-configuration)
- [Ollama documentation](https://docs.ollama.com/)
