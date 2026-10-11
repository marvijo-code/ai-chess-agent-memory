# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 245 | 3192235 | 1879552 | 58.9% | 58.7% |
| GPT-6.1 Sol | 164 | 4875188 | 4475648 | 91.8% | 92.6% |
| Sonnet 5.5 | 210 | 6054891 | 5829835 | 96.3% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8315 | 93127016 | 48036864 | 51.6% | 51.5% |
| GPT-6.1 Sol | 6635 | 193391848 | 180032000 | 93.1% | 93.6% |
| Sonnet 5.5 | 6744 | 148658704 | 141894975 | 95.5% | 96.1% |
