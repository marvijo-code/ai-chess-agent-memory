# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 158 | 1714439 | 895232 | 52.2% | 52.2% |
| GPT-6.1 Sol | 158 | 5383332 | 4992512 | 92.7% | 93.1% |
| Sonnet 5.5 | 145 | 3352072 | 3207741 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1049 | 11609116 | 5440128 | 46.9% | 46.8% |
| GPT-6.1 Sol | 866 | 25800143 | 24131456 | 93.5% | 93.9% |
| Sonnet 5.5 | 936 | 21450419 | 20553235 | 95.8% | 96.3% |
