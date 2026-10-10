# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 298 | 3369830 | 1611904 | 47.8% | 47.7% |
| GPT-6.1 Sol | 224 | 6815091 | 6385792 | 93.7% | 94.3% |
| Sonnet 5.5 | 237 | 5297731 | 5070573 | 95.7% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4800 | 52897266 | 25294080 | 47.8% | 47.8% |
| GPT-6.1 Sol | 3893 | 112180308 | 104160128 | 92.9% | 93.3% |
| Sonnet 5.5 | 4134 | 91068089 | 86971321 | 95.5% | 96.1% |
