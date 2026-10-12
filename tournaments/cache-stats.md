# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 93 | 1336509 | 1209984 | 90.5% | 91.5% |
| GLM 5.3 Flash | 54 | 487488 | 398080 | 81.7% | 83.0% |
| GPT-6.1 Sol | 76 | 2301437 | 2120448 | 92.1% | 92.9% |
| Sonnet 5.5 | 119 | 3018022 | 2883635 | 95.5% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8635 | 97326310 | 50629248 | 52.0% | 52.0% |
| GLM 5.3 Flash | 54 | 487488 | 398080 | 81.7% | 83.0% |
| GPT-6.1 Sol | 7051 | 206489790 | 192186624 | 93.1% | 93.6% |
| Sonnet 5.5 | 7124 | 157987779 | 150794672 | 95.4% | 96.1% |
