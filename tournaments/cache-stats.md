# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 69 | 1129641 | 1073536 | 95.0% | 96.1% |
| Fable 5.1 | 45 | 517329 | 468275 | 90.5% | 92.0% |
| GLM 5.3 Flash | 26 | 293535 | 270656 | 92.2% | 93.8% |
| GPT-6 Astra | 97 | 3976109 | 3844352 | 96.7% | 96.8% |
| GPT-6.1 Sol | 100 | 3732022 | 3503232 | 93.9% | 94.4% |
| Sonnet 5.5 | 100 | 3136730 | 3032706 | 96.7% | 97.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9165 | 106113708 | 58724352 | 55.3% | 55.3% |
| Fable 5.1 | 45 | 517329 | 468275 | 90.5% | 92.0% |
| GLM 5.3 Flash | 479 | 6799214 | 5990400 | 88.1% | 88.8% |
| GPT-6 Astra | 97 | 3976109 | 3844352 | 96.7% | 96.8% |
| GPT-6.1 Sol | 7936 | 237785648 | 221549824 | 93.2% | 93.7% |
| Sonnet 5.5 | 7937 | 180570570 | 172510766 | 95.5% | 96.2% |
