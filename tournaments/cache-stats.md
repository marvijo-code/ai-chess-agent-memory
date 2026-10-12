# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 168 | 3159447 | 2950656 | 93.4% | 94.2% |
| GLM 5.3 Flash | 165 | 2721186 | 2480896 | 91.2% | 91.8% |
| GPT-6.1 Sol | 170 | 5543146 | 5127680 | 92.5% | 93.4% |
| Sonnet 5.5 | 161 | 4138752 | 3961335 | 95.7% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9045 | 104344766 | 57094656 | 54.7% | 54.7% |
| GLM 5.3 Flash | 453 | 6505679 | 5719744 | 87.9% | 88.6% |
| GPT-6.1 Sol | 7594 | 223053902 | 207510784 | 93.0% | 93.5% |
| Sonnet 5.5 | 7742 | 174675223 | 166818297 | 95.5% | 96.2% |
