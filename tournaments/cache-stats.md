# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| Fable 5.1 | 23 | 230958 | 207909 | 90.0% | 91.2% |
| GLM 5.3 Flash | 26 | 293535 | 270656 | 92.2% | 93.8% |
| GPT-6.1 Sol | 23 | 459445 | 396800 | 86.4% | 87.0% |
| Sonnet 5.5 | 27 | 577569 | 540786 | 93.6% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9096 | 104984067 | 57650816 | 54.9% | 54.9% |
| Fable 5.1 | 23 | 230958 | 207909 | 90.0% | 91.2% |
| GLM 5.3 Flash | 479 | 6799214 | 5990400 | 88.1% | 88.8% |
| GPT-6.1 Sol | 7859 | 234513071 | 218443392 | 93.1% | 93.6% |
| Sonnet 5.5 | 7864 | 178011409 | 170018846 | 95.5% | 96.2% |
