# HaixiuZu APP Server DB Description

| Version | Author |Date | Changelog |
| ---- | ---- | ---- | ---- |
| 0.1 | Derek Luo | 2014-07-24 | Created |


## user
* primary_key :  _id
* user_level : Default 5, User has permission to read topics that user_level >= topic_level

| Name | Type | Default | Description |
| ---- | ---- | ---- | ---- |
| _id | ObjectId | key | app internal user_id |
| created_ts | Long | | timestamp that user first login app|
| user_level | Int | 5 | 0 - 9 |
| name | String | None | nickname, init from douban |
| desc | String | None | user description, init from douban |
| homepage | String | None | user homepage of douban |
| avatar | String | None | |
| photo_wall | String | None | list to string |
| photo_wall_tiny | String | None | list to string |
| updated_ts | Long | | timestamp that user profile been updated latest |
| liked_topics | List | [] | list of topics that user liked, sort by recent action | 
| commented_topics | List | [] | list of topics that user published comment, sort by recent action |

## user_map
* primary_key :  user_id & douban_id

| Name | Type | Default | Description |
| ---- | ---- | ---- | ---- |
| user_id | ObjectId | key | app internal user_id |
| app_id | String | auto-increment | like QQ, 8 bit number |
| douban_id | String | None | init from douban |
| weibo_id | String | None | |
| qq_id | String | None | |


## user_relation
* primary_key : user_id
| Name | Type | Default | Description |
| ---- | ---- | ---- | ---- |
| user_id | ObjectId | key | app internal user_id |
| friend_id | ObjectId | key | app internal user_id |
| relation_type | Int | 0 | 0: friend, 1: black list |


## topic
* primary_key : _id
* topic_level : Default 5, User has permission to read topics that user_level >= topic_level, if this topic been deleted, topic_level++

Name | Type | Default | Description |
| ---- | ---- | ---- | ---- |
| _id | ObjectId | key | app internal topic_id |
| created_ts | Long | | timestamp that topic been created |
| topic_level | Int | 5 | 0 - 9 |
| author | Dictionary | | profile of author when publish topic |
| author.user_id | ObjectId | | app internal user_id |
| author.name | String | | nickname when publish topic |
| author.avatar | String | | |
| author.user_level | Int | | |
| updated_ts | Long | | timestamp that topic been updated latest | 
| title | String | | topic title with "shai" |
| content | String | | content with special mark of DOUBAN picture |
| topic_photos | String | | list to string |
| topic_photos_tiny | String | | list to string |
| comment_count | Int | 0 | |
| liked_users | List | [] | list of user id who liked this topic |
| like_count | Int | 0 | |
| burn_ts | Long | | timestamp that user prefers to burn this topic |
| action_ts | Long | | timestamp that latest action take, include like comment and so on |


## comment
* primary_key: 

| Name | Type | Default | Description |
| ---- | ---- | ---- | ---- |
| | | | |






