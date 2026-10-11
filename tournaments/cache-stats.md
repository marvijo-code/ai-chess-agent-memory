# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 293 | 3332660 | 2023936 | 60.7% | 60.8% |
| GPT-6.1 Sol | 208 | 5849351 | 5435136 | 92.9% | 93.4% |
| Sonnet 5.5 | 212 | 4623910 | 4405205 | 95.3% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6188 | 68836131 | 34274304 | 49.8% | 49.7% |
| GPT-6.1 Sol | 4982 | 143515822 | 133497344 | 93.0% | 93.5% |
| Sonnet 5.5 | 5244 | 116053213 | 110840908 | 95.5% | 96.1% |
