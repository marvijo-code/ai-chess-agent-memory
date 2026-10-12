# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 192 | 3441039 | 3183488 | 92.5% | 93.4% |
| GLM 5.3 Flash | 165 | 2721186 | 2480896 | 91.2% | 91.8% |
| GPT-6.1 Sol | 191 | 5946317 | 5492736 | 92.4% | 93.3% |
| Sonnet 5.5 | 181 | 4486948 | 4281585 | 95.4% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9069 | 104626358 | 57327488 | 54.8% | 54.8% |
| GLM 5.3 Flash | 453 | 6505679 | 5719744 | 87.9% | 88.6% |
| GPT-6.1 Sol | 7615 | 223457073 | 207875840 | 93.0% | 93.5% |
| Sonnet 5.5 | 7762 | 175023419 | 167138547 | 95.5% | 96.2% |
