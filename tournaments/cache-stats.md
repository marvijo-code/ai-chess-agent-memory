# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 187 | 1805852 | 788096 | 43.6% | 43.6% |
| GPT-6.1 Sol | 244 | 8439162 | 7807104 | 92.5% | 93.0% |
| Sonnet 5.5 | 224 | 4789831 | 4561611 | 95.2% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2447 | 26905202 | 12184448 | 45.3% | 45.2% |
| GPT-6.1 Sol | 2076 | 62071620 | 57820544 | 93.2% | 93.6% |
| Sonnet 5.5 | 2191 | 49383989 | 47228130 | 95.6% | 96.2% |
