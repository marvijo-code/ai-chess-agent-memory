# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 69 | 1129641 | 1073536 | 95.0% | 96.1% |
| Fable 5.1 | 45 | 517329 | 468275 | 90.5% | 92.0% |
| GLM 5.3 Flash | 26 | 293535 | 270656 | 92.2% | 93.8% |
| GPT-6 Astra | 97 | 3976109 | 3844352 | 96.7% | 96.8% |
| GPT-6.1 Sol | 71 | 1861625 | 1682432 | 90.4% | 91.3% |
| Sonnet 5.5 | 71 | 1763634 | 1678747 | 95.2% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9165 | 106113708 | 58724352 | 55.3% | 55.3% |
| Fable 5.1 | 45 | 517329 | 468275 | 90.5% | 92.0% |
| GLM 5.3 Flash | 479 | 6799214 | 5990400 | 88.1% | 88.8% |
| GPT-6 Astra | 97 | 3976109 | 3844352 | 96.7% | 96.8% |
| GPT-6.1 Sol | 7907 | 235915251 | 219729024 | 93.1% | 93.6% |
| Sonnet 5.5 | 7908 | 179197474 | 171156807 | 95.5% | 96.2% |
