# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 56 | 541378 | 243072 | 44.9% | 44.7% |
| GPT-6.1 Sol | 43 | 1186385 | 1103232 | 93.0% | 93.3% |
| Sonnet 5.5 | 47 | 1031701 | 984407 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4856 | 53438644 | 25537152 | 47.8% | 47.7% |
| GPT-6.1 Sol | 3936 | 113366693 | 105263360 | 92.9% | 93.3% |
| Sonnet 5.5 | 4181 | 92099790 | 87955728 | 95.5% | 96.1% |
