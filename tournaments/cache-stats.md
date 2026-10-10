# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 248 | 2827984 | 1401728 | 49.6% | 49.5% |
| GPT-6.1 Sol | 155 | 4002111 | 3739008 | 93.4% | 93.9% |
| Sonnet 5.5 | 162 | 3277406 | 3112905 | 95.0% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3855 | 41963823 | 19521152 | 46.5% | 46.4% |
| GPT-6.1 Sol | 3285 | 95619902 | 88866176 | 92.9% | 93.4% |
| Sonnet 5.5 | 3456 | 76900364 | 73466687 | 95.5% | 96.1% |
