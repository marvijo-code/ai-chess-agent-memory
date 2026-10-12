# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 144 | 2086317 | 1886592 | 90.4% | 91.6% |
| GLM 5.3 Flash | 134 | 1650640 | 1399040 | 84.8% | 85.6% |
| GPT-6.1 Sol | 201 | 6305418 | 5902208 | 93.6% | 94.2% |
| Sonnet 5.5 | 290 | 8074607 | 7772889 | 96.3% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8686 | 98076118 | 51305856 | 52.3% | 52.3% |
| GLM 5.3 Flash | 134 | 1650640 | 1399040 | 84.8% | 85.6% |
| GPT-6.1 Sol | 7176 | 210493771 | 195968384 | 93.1% | 93.6% |
| Sonnet 5.5 | 7295 | 163044364 | 155683926 | 95.5% | 96.2% |
