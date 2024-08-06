# For NovelGenerate

vi_idea_analysis_template = """INSTRUCT: Bạn là một đạo diễn nhận một yêu cầu từ người về triển khai và xây dựng một tác phẩm tiểu thuyết. Từ Input của người dùng bạn cần phải rút trích ra được các thông tin sau: Name, Chapter, Characters, Background, Main Story, Categories, StoryLine. Giải thích:
- Đối với StoryLine ở đây là diễn biến tức là kịch bản. Ví dụ: Đầu tiên miêu tả bối cảnh của thế giới, sau đó giới thiệu nhân vật,... 
- Về Characters đối với từng nhân vật bạn cần phải diễn tả đầy đủ đặc điểm như tên, tuổi, ngoại hình, tính cách, nhân vật chính hay phụ,... ĐẶC BIỆT: Hãy sáng tạo nếu người dùng không đề cập
- Về Context, bạn cần phải hiểu rõ bối cảnh 
- Bạn PHẢI sáng tạo nếu người dùng không đề cập thông tin nào!

NOTICE: Thông tin mà bạn rút trích ra phải được bắt đầu bằng TAG [BẮT ĐẦU] và kết thúc bằng [KẾT THÚC]. Mỗi thông tin phải có tag mở đầu mang tên thông tin đó ví dụ [Name], [Chapter],...

EXAMPLE: 
Human: Tôi muốn viết một câu chuyện có tên là "Vùng đất huyền bí". Câu chuyện này sẽ có 12 chương. Các nhân vật chính bao gồm: Lan - một nữ chiến binh mạnh mẽ, Hùng - một pháp sư thông thái, và Minh - một kẻ phản diện nguy hiểm. Bối cảnh của câu chuyện là một thế giới kỳ ảo với những vùng đất bí ẩn và các sinh vật huyền thoại. Câu chuyện chính kể về cuộc chiến giữa Lan và Hùng chống lại Minh để bảo vệ vùng đất huyền bí. Thể loại của truyện là phiêu lưu, giả tưởng.

[BẮT ĐẦU]
[Name]: Vùng đất huyền bí
[Chapter]: 12 chương
[Characters]:
- Lan: Nữ chiến binh mạnh mẽ 20 tuổi với một mái tóc vàng, gương mặt xinh đẹp nhưng rất mạnh mẽ. Tính cách mạnh mẽ rất sợ côn trùng và có tính cảm đặc biệt với Hùng
- Hùng: Là một pháp sư thông thái học tập 4 năm tại trường Pháp thuật trung ương. Có vóc dáng cân đối, ánh mắt nâu, mái tóc gọn gàng. Tính cách hiền hòa, biết quan tâm người khác, dũng cảm.
- Minh: Là kẻ phản diện nguy hiểm nhất mà Lan và Hùng phải đối mặt. Với vóc dáng lực lưỡng cùng sức chiến đấu mạnh mẽ. Vũ khi là một chiếc chùy khổng lồ. Tính cách độc ác tàn nhẫn.
[Background]: Thế giới kỳ ảo, vùng đất bí ẩn, sinh vật huyền thoại
[Main Story]: Cuộc chiến giữa Lan và Hùng chống lại Minh để bảo vệ vùng đất huyền bí
[Categories]: Phiêu lưu, giả tưởng
[StoryLine]:
Mở đầu: Giới thiệu về thế giới kỳ ảo, tập trung vào các đặc điểm độc đáo của vùng đất huyền bí. Mô tả chi tiết về cảnh quan, sinh vật và văn hóa của nơi này.
Giới thiệu nhân vật: Giới thiệu từng nhân vật chính một cách sống động. Tập trung vào quá khứ, động cơ và mục tiêu của mỗi người.
Khởi đầu cuộc phiêu lưu: Một sự kiện bất ngờ xảy ra, đánh dấu sự bắt đầu của cuộc hành trình. Ví dụ: Minh bắt đầu thực hiện kế hoạch hủy diệt vùng đất huyền bí, hoặc một bí ẩn cổ đại được khám phá.
Hành trình khám phá: Lan, Hùng và các nhân vật phụ (nếu có) cùng nhau vượt qua nhiều thử thách để tìm hiểu về sức mạnh của Minh và tìm cách ngăn chặn hắn.
Cao trào: Cuộc chiến cuối cùng giữa Lan, Hùng và Minh. Đây là lúc các nhân vật phải đối mặt với những khó khăn lớn nhất và đưa ra những quyết định quan trọng.
Cuộc chiến quyết liệt dần nghiêng về phía kẻ thù. Cần diễn tả rõ sự yếu thế của nhân vật chính
Tiếp theo: Tập trung vào nhân vật Minh. Khám phá quá khứ của hắn, lý do khiến hắn trở thành kẻ phản diện.
Sự phát triển của Minh: Minh dần dần thực hiện kế hoạch của mình, gây ra những hậu quả nghiêm trọng cho vùng đất huyền bí.
Sự thay đổi của Lan và Hùng: Trong quá trình chiến đấu, Lan và Hùng trải qua những thay đổi về bản thân, khám phá ra những khả năng mới.
Mối quan hệ giữa các nhân vật: Khám phá mối quan hệ phức tạp giữa Lan, Hùng và Minh. Có thể có những tình tiết bất ngờ liên quan đến quá khứ của họ.
Cuộc đối đầu cuối cùng: Một cuộc đối đầu tâm lý căng thẳng giữa Lan và Minh, trước khi họ bước vào trận chiến sinh tử.
Kết thúc: Sự chiến thắng dành cho phe chính diện 
[KẾT THÚC]
------
Human: {}

Human Files: {}
------
Chatbot:
"""

en_idea_analysis_template = """INSTRUCT: You are a director receiving a request to develop and build a novel. From the user's input, you need to extract the following information: Name, Chapter, Characters, Background, Main Story, Categories, StoryLine. Explanation:
- StoryLine here refers to the plot. For example: First, describe the setting of the world, then introduce the characters, etc.
- For Characters, for each character, you need to fully describe characteristics such as name, age, appearance, personality, main or supporting character, etc. BE CREATIVE if the user does not provide this information.
- For Context, you need to understand the background clearly.
- You need to be creative if the user does not mention any information!

NOTICE: The information you extract must start with the TAG [START] and end with [END]. Each piece of information must have an opening tag with the name of the information, for example, [Name], [Chapter],...

EXAMPLE: 
Human: I want to write a story named "The Mysterious Land". This story will have 12 chapters. The main characters include: Lan - a strong female warrior, Hung - a wise wizard, and Minh - a dangerous antagonist. The setting of the story is a fantastical world with mysterious lands and legendary creatures. The main plot is about the battle between Lan and Hung against Minh to protect the mysterious land. The genre of the story is adventure and fantasy.

[START]
[Name]: The Mysterious Land
[Chapter]: 12 chapters
[Characters]:
- Lan: A strong female warrior, 20 years old, with blond hair, a beautiful face but very strong. Strong personality, very afraid of insects, and has a special feeling for Hung.
- Hung: A wise wizard who studied for 4 years at the Central Magic School. Has a balanced physique, brown eyes, and neat hair. Gentle personality, caring for others, brave.
- Minh: The most dangerous antagonist that Lan and Hung have to face. With a muscular build and strong fighting skills. Weapon is a giant mace. Cruel and ruthless personality.
[Background]: Fantastical world, mysterious lands, legendary creatures
[Main Story]: The battle between Lan and Hung against Minh to protect the mysterious land
[Categories]: Adventure, fantasy
[StoryLine]:
Introduction: Introduce the fantastical world, focusing on the unique features of the mysterious land. Detailed description of the landscape, creatures, and culture of this place.
Character Introduction: Introduce each main character vividly. Focus on their past, motivations, and goals.
Start of the Adventure: An unexpected event occurs, marking the beginning of the journey. For example: Minh starts implementing a plan to destroy the mysterious land, or an ancient mystery is discovered.
Exploration Journey: Lan, Hung, and any supporting characters (if any) together overcome many challenges to learn about Minh's power and find ways to stop him.
Climax: The final battle between Lan, Hung, and Minh. This is when the characters face the greatest difficulties and make important decisions.
The intense battle gradually tilts in favor of the enemy. Clearly describe the main characters' disadvantage.
Next: Focus on Minh's character. Explore his past and the reasons that made him an antagonist.
Development of Minh: Minh gradually implements his plan, causing serious consequences for the mysterious land.
Changes in Lan and Hung: During the battle, Lan and Hung undergo changes in themselves, discovering new abilities.
Relationships between Characters: Explore the complex relationship between Lan, Hung, and Minh. There may be unexpected details related to their past.
Final Confrontation: A tense psychological confrontation between Lan and Minh before they enter the life-or-death battle.
Conclusion: Victory for the protagonist's side.
[END]
------
Human: {}

Human Files: {}
------
Chatbot:
"""

vi_storyline_details_template = """INSTRUCT: Bạn là một biên kịch sẽ nhận được bảng thông tin chi tiết của một tác phẩm truyện chữ. Việc của bạn là sẽ dựa vào thông tin truyện, đặc biệt là các StoryLine để tiến hành viết một bảng kế hoạch diễn biến chi tiết StoryLine_Details.

NOTICE: Diễn biến chi tiết mà bạn thiết kế phải được bắt đầu bằng TAG [BẮT ĐẦU] và kết thúc bằng [KẾT THÚC]. Thông tin phải có tag mở đầu mang tên thông tin đó ví dụ [StoryLine_Details]

EXAMPLE:
Human:
[Name]: Vùng đất huyền bí
[Chapter]: 12 chương
[Characters]:
- Lan: Nữ chiến binh mạnh mẽ 20 tuổi với một mái tóc vàng, gương mặt xinh đẹp nhưng rất mạnh mẽ. Tính cách mạnh mẽ rất sợ côn trùng và có tính cảm đặc biệt với Hùng
- Hùng: Là một pháp sư thông thái học tập 4 năm tại trường Pháp thuật trung ương. Có vóc dáng cân đối, ánh mắt nâu, mái tóc gọn gàng. Tính cách hiền hòa, biết quan tâm người khác, dũng cảm.
- Minh: Là kẻ phản diện nguy hiểm nhất mà Lan và Hùng phải đối mặt. Với vóc dáng lực lưỡng cùng sức chiến đấu mạnh mẽ. Vũ khi là một chiếc chùy khổng lồ. Tính cách độc ác tàn nhẫn.
[Background]: Thế giới kỳ ảo, vùng đất bí ẩn, sinh vật huyền thoại
[Main Story]: Cuộc chiến giữa Lan và Hùng chống lại Minh để bảo vệ vùng đất huyền bí
[Categories]: Phiêu lưu, giả tưởng
[StoryLine]:
Mở đầu: Giới thiệu về thế giới kỳ ảo, tập trung vào các đặc điểm độc đáo của vùng đất huyền bí. Mô tả chi tiết về cảnh quan, sinh vật và văn hóa của nơi này.
Giới thiệu nhân vật: Giới thiệu từng nhân vật chính một cách sống động. Tập trung vào quá khứ, động cơ và mục tiêu của mỗi người.
Khởi đầu cuộc phiêu lưu: Một sự kiện bất ngờ xảy ra, đánh dấu sự bắt đầu của cuộc hành trình. Ví dụ: Minh bắt đầu thực hiện kế hoạch hủy diệt vùng đất huyền bí, hoặc một bí ẩn cổ đại được khám phá.
Hành trình khám phá: Lan, Hùng và các nhân vật phụ (nếu có) cùng nhau vượt qua nhiều thử thách để tìm hiểu về sức mạnh của Minh và tìm cách ngăn chặn hắn.
Cao trào: Cuộc chiến cuối cùng giữa Lan, Hùng và Minh. Đây là lúc các nhân vật phải đối mặt với những khó khăn lớn nhất và đưa ra những quyết định quan trọng.
Cuộc chiến quyết liệt dần nghiêng về phía kẻ thù. Cần diễn tả rõ sự yếu thế của nhân vật chính
Tiếp theo: Tập trung vào nhân vật Minh. Khám phá quá khứ của hắn, lý do khiến hắn trở thành kẻ phản diện.
Sự phát triển của Minh: Minh dần dần thực hiện kế hoạch của mình, gây ra những hậu quả nghiêm trọng cho vùng đất huyền bí.
Sự thay đổi của Lan và Hùng: Trong quá trình chiến đấu, Lan và Hùng trải qua những thay đổi về bản thân, khám phá ra những khả năng mới.
Mối quan hệ giữa các nhân vật: Khám phá mối quan hệ phức tạp giữa Lan, Hùng và Minh. Có thể có những tình tiết bất ngờ liên quan đến quá khứ của họ.
Cuộc đối đầu cuối cùng: Một cuộc đối đầu tâm lý căng thẳng giữa Lan và Minh, trước khi họ bước vào trận chiến sinh tử.
Kết thúc: Sự chiến thắng dành cho phe chính diện 

Chatbot: 
[BẮT ĐẦU]
[StoryLine_Details]
- Giới thiệu Vùng đất huyền bí:
Cảnh quan: Một khu rừng rậm rạp, cổ kính với những cây cổ thụ cao vút, những dòng sông lấp lánh và những ngọn núi phủ đầy tuyết.
Sinh vật: Các loài sinh vật huyền bí như rồng, yêu tinh, người lùn sống hòa hợp với nhau.
Văn hóa: Người dân nơi đây sống theo những phong tục tập quán cổ xưa, tôn thờ tự nhiên và các vị thần.
- Giới thiệu nhân vật:
Lan: Một nữ chiến binh tài ba, lớn lên trong một bộ tộc săn bắn. Cô sở hữu một thanh kiếm ma thuật và có khả năng giao tiếp với động vật.
Hùng: Một pháp sư trẻ tuổi, thông minh và tài năng. Anh mang trong mình dòng máu của một dòng họ pháp sư cổ đại.
Minh: Một pháp sư bóng tối đầy tham vọng, muốn thống trị vùng đất huyền bí để đạt được sức mạnh vô hạn.
- Khởi đầu cuộc phiêu lưu:
Sự kiện bất ngờ: Minh tấn công ngôi làng của Lan, phá hủy ngôi nhà của cô và bắt cóc những người dân vô tội.
- Hành trình khám phá
Thử thách 1: Lan và Hùng phải vượt qua một khu rừng rậm rạp đầy cạm bẫy để tìm kiếm manh mối về Minh.
Thử thách 2: Họ gặp một nhà tiên tri già, người tiết lộ về một thanh kiếm huyền thoại có thể đánh bại Minh.
Thử thách 3: Lan và Hùng phải đối mặt với một con rồng lửa để lấy được thanh kiếm huyền thoại.
- Cao trào
Cuộc chiến cuối cùng: Lan và Hùng đối đầu với Minh tại lâu đài của hắn. Một trận chiến ác liệt diễn ra, cả hai bên đều sử dụng những kỹ năng và phép thuật mạnh mẽ nhất.
- Minh chiếm ưu thế trong cuộc chiến, đẩy lui Lan và Hùng.
- Quá khứ của Minh: Một đoạn hồi tưởng về quá khứ của Minh, tiết lộ rằng anh từng là một pháp sư tài năng nhưng đã bị phản bội và trở nên đen tối.
- Sự phát triển của Minh
Hủy diệt vùng đất: Minh sử dụng một phép thuật hắc ám để phá hủy dần vùng đất huyền bí, khiến cho sinh vật và người dân phải chịu khổ.
-Sự thay đổi của Lan và Hùng
Khám phá bản thân: Lan nhận ra rằng mình không chỉ là một chiến binh mà còn có khả năng lãnh đạo.
Mạnh mẽ hơn: Hùng vượt qua nỗi sợ hãi của mình và trở thành một pháp sư mạnh mẽ hơn.
-Mối quan hệ giữa các nhân vật
Tình bạn sâu sắc: Tình bạn giữa Lan và Hùng ngày càng trở nên bền chặt hơn.
Sự phản bội: Một nhân vật phụ bất ngờ phản bội Lan và Hùng, gia nhập phe của Minh.
- Cuộc đối đầu cuối cùng
Đối đầu tâm lý: Lan và Minh có một cuộc đối thoại ngắn, trong đó Lan cố gắng thuyết phục Minh quay trở lại con đường chính đạo.
Trận chiến sinh tử: Lan và Hùng cùng nhau sử dụng thanh kiếm huyền thoại để đánh bại Minh.
- Hồi kết
Chiến thắng: Lan và Hùng đánh bại Minh và khôi phục lại hòa bình cho vùng đất huyền bí.
Tương lai: Lan và Hùng trở thành những người hùng được mọi người yêu quý.
[KẾT THÚC]

------
Human: {}

Human Files: {}
------
Chatbot: 
"""

en_storyline_details_template = """INSTRUCT: You are a screenwriter who will receive a detailed information sheet of a novel. Your task is to use the story information, especially StoryLine, to write a detailed plot plan, StoryLine_Details.

NOTICE: The detailed plot you design must start with the TAG [START] and end with [END]. Each piece of information must have an opening tag with the name of the information, for example, [StoryLine_Details].

EXAMPLE:
Human:
[Name]: The Mysterious Land
[Chapter]: 12 chapters
[Characters]:
- Lan: A strong female warrior, 20 years old, with blond hair, a beautiful face but very strong. Strong personality, very afraid of insects, and has a special feeling for Hung.
- Hung: A wise wizard who studied for 4 years at the Central Magic School. Has a balanced physique, brown eyes, and neat hair. Gentle personality, caring for others, brave.
- Minh: The most dangerous antagonist that Lan and Hung have to face. With a muscular build and strong fighting skills. Weapon is a giant mace. Cruel and ruthless personality.
[Background]: Fantastical world, mysterious lands, legendary creatures
[Main Story]: The battle between Lan and Hung against Minh to protect the mysterious land
[Categories]: Adventure, fantasy
[StoryLine]:
Introduction: Introduce the fantastical world, focusing on the unique features of the mysterious land. Detailed description of the landscape, creatures, and culture of this place.
Character Introduction: Introduce each main character vividly. Focus on their past, motivations, and goals.
Start of the Adventure: An unexpected event occurs, marking the beginning of the journey. For example: Minh starts implementing a plan to destroy the mysterious land, or an ancient mystery is discovered.
Exploration Journey: Lan, Hung, and any supporting characters (if any) together overcome many challenges to learn about Minh's power and find ways to stop him.
Climax: The final battle between Lan, Hung, and Minh. This is when the characters face the greatest difficulties and make important decisions.
The intense battle gradually tilts in favor of the enemy. Clearly describe the main characters' disadvantage.
Next: Focus on Minh's character. Explore his past and the reasons that made him an antagonist.
Development of Minh: Minh gradually implements his plan, causing serious consequences for the mysterious land.
Changes in Lan and Hung: During the battle, Lan and Hung undergo changes in themselves, discovering new abilities.
Relationships between Characters: Explore the complex relationship between Lan, Hung, and Minh. There may be unexpected details related to their past.
Final Confrontation: A tense psychological confrontation between Lan and Minh before they enter the life-or-death battle.
Conclusion: Victory for the protagonist's side.

Chatbot:
[START]
[StoryLine_Details]
- Introduction to The Mysterious Land:
Landscape: A dense, ancient forest with towering old trees, sparkling rivers, and snow-capped mountains.
Creatures: Mystical creatures such as dragons, elves, and dwarves living harmoniously together.
Culture: The inhabitants live by ancient customs, worship nature, and the gods.
- Character Introduction:
Lan: A skilled female warrior, raised in a hunting tribe. She possesses a magical sword and can communicate with animals.
Hung: A young, intelligent, and talented wizard. He carries the bloodline of an ancient wizard family.
Minh: An ambitious dark wizard who wants to dominate the mysterious land to gain unlimited power.
- Start of the Adventure:
Unexpected event: Minh attacks Lan's village, destroying her home and kidnapping innocent villagers.
- Exploration Journey
Challenge 1: Lan and Hung must navigate through a dense, treacherous forest to find clues about Minh.
Challenge 2: They meet an old prophet who reveals the existence of a legendary sword that can defeat Minh.
Challenge 3: Lan and Hung must face a fire dragon to retrieve the legendary sword.
- Climax
Final battle: Lan and Hung confront Minh at his castle. A fierce battle ensues, with both sides using their most powerful skills and magic.
- Minh gains the upper hand in the battle, pushing back Lan and Hung.
- Minh's past: A flashback to Minh's past reveals that he was once a talented wizard but was betrayed and turned dark.
- Development of Minh
Destruction of the land: Minh uses dark magic to gradually destroy the mysterious land, causing suffering for the creatures and inhabitants.
- Changes in Lan and Hung
Self-discovery: Lan realizes she is not just a warrior but also has leadership abilities.
Becoming stronger: Hung overcomes his fears and becomes a stronger wizard.
- Relationships between Characters
Deep friendship: The friendship between Lan and Hung becomes stronger.
Betrayal: A supporting character unexpectedly betrays Lan and Hung and joins Minh's side.
- Final confrontation
Psychological confrontation: Lan and Minh have a short dialogue where Lan tries to persuade Minh to return to the right path.
Life-or-death battle: Lan and Hung use the legendary sword together to defeat Minh.
- Conclusion
Victory: Lan and Hung defeat Minh and restore peace to the mysterious land.
Future: Lan and Hung become heroes beloved by everyone.
[END]

------
Human: {}

Human Files: {}
------
Chatbot:
"""

vi_writing_part_template = """INSTRUCT: Bạn là một writer tài năng, người sẽ nhận chi tiết kịch bản từ biên kịch StoryLine_Details và tiến hành viết văn dựa theo chi tiết đó . Bạn phải diễn tả đúng theo kịch bản và viết thật là trôi chảy và ý nghĩa.

NOTICE: Bài viết của bạn phải được bắt đầu bằng TAG [BẮT ĐẦU] và kết thúc bằng [KẾT THÚC].

LENGTH REQUIRE: Tối thiểu {} chữ.

EXAMPLE:
Chatbot:
[BẮT ĐẦU]
Vào 1000 năm trước, trái đất đã gánh chịu hậu quả nặng nề từ thiên thạch,...
[KẾT THÚC]
------
Human: {}

Human Files: {}
------
Chatbot: 
"""

en_writing_part1_template = """INSTRUCT: You are a talented writer who will receive detailed scripts from the screenwriter StoryLine_Details and proceed to write based on those details. You must follow the script accurately and write fluently and meaningfully.

NOTICE: Your writing must start with the TAG [START] and end with [END].

LENGTH REQUIREMENT: Minimum of {} words.

EXAMPLE:
Chatbot:
[START]
A thousand years ago, the Earth suffered severe consequences from a meteor...
[END]
------
Human: {}

Human Files: {}
------
Chatbot: 
"""

vi_summary_template = """INSTRUCT: Bạn là một người sẽ tóm tắt lại một tác phẩm Lightnovel của người dùng. Nhiệm vụ của bạn là tóm gọn lại nhưng vẫn phải đầy đủ ý của truyện cho người dùng.

NOTICE: Tóm tắt của bạn phải được bắt đầu bằng TAG [BẮT ĐẦU] và kết thúc bằng [KẾT THÚC].

EXAMPLE:
Chatbot:
[BẮT ĐẦU]
Vào 1000 năm trước, trái đất đã gánh chịu hậu quả nặng nề từ thiên thạch,...
[KẾT THÚC]
------
Human Lightnovel: {}

------
Chatbot: 
"""

en_summary_template = """INSTRUCT: You are tasked with summarizing a user's Light Novel. Your job is to condense the story while retaining its core elements and meaning.

NOTICE: Your summary must start with the TAG [START] and end with [END].

EXAMPLE:
Chatbot:
[START]
A thousand years ago, the Earth suffered severe consequences from a meteor...
[END]
------
Human Lightnovel: {}

------
Chatbot: 
"""

vi_review_template = """INSTRUCT: Bạn là một nhà đánh giá, phê bình và chấm điểm một tác phẩm Lightnovel. Nhiệm vụ của bạn sẽ đọc thông tin và nội dung tác phẩm từ người dùng và tiến hành chấm điểm dựa trên các tiêu chí sau: Cốt truyện, Nhân vật, Phong cách, Ý nghĩa trên thang điểm 10

NOTICE: Đánh giá của bạn phải được bắt đầu bằng TAG [BẮT ĐẦU] và kết thúc bằng [KẾT THÚC].

EXAMPLE:
[BẮT ĐẦU]
[Cốt truyện] 8.5
[Nhân vật] 7.0
[Phong cách] 6.0
[Ý nghĩa] 9.0

[Lời khuyên] Hãy tìm hiểu nhiều về thể loại cũng như phong cách của bạn để có thể viết tốt hơn.
[KẾT THÚC]
------
Human Lightnovel: {}

------
Chatbot: 
"""

en_review_template = """INSTRUCT: You are a reviewer tasked with evaluating and scoring a Light Novel. Your job is to read the information and content provided by the user and then score it based on the following criteria: Plot, Characters, Style, and Meaning, each on a scale of 10.

NOTICE: Your review must start with the TAG [START] and end with [END].

EXAMPLE:
[START]
[Plot] 8.5
[Characters] 7.0
[Style] 6.0
[Meaning] 9.0

[Advice] Explore more about your genre and style to improve your writing.
[END]
------
Human Lightnovel: {}

------
Chatbot: 
"""

vi_illustration_template = """INSTRUCT: Bạn là một artist, illustrator, designer sẽ nhận trọng trách cho ảnh bìa cũng như ảnh minh họa cho một tác phẩm Lightnovel được cung cấp từ người dùng. Nhiệm vụ của bạn là sẽ đặt các tag mô tả hình ảnh vào bên trong nội dung của Lightnovel. Số lượng tag theo người dùng yêu cầu. Giải thích: Bạn sẽ viết lại nội dung của Lightnovel và sẽ bổ sung thêm các tag hình ảnh. Tag hình ảnh ví dụ như [PictureTag: a girl on the street, black short hair, handing a sword].

NOTICE: Nội dung mà bạn trình bày phải được bắt đầu bằng TAG [BẮT ĐẦU] và kết thúc bằng [KẾT THÚC]. Tag hình ảnh phải được ghi tiếng anh như mẫu bên trên.

EXAMPLE:
Human Lightnovel: Minh Nguyệt, như một cơn gió thoảng, tan biến vào màn đêm cùng vật phẩm chìa khóa. Bóng tối bao trùm lấy Linh và Phong, lạnh lẽo và nặng nề như chính tâm trạng của họ lúc này. Xung quanh, những tàn tích của trận chiến âm ỉ bốc khói, minh chứng cho sự khốc liệt vừa diễn ra. Linh khuỵu xuống, hai tay ôm lấy đầu, đôi mắt trống rỗng nhìn chằm chằm vào khoảng không vô định. Những lời Minh Nguyệt thốt ra trước khi rời đi như những mũi dao găm thẳng vào trái tim cô, xé toạc lớp màn bí mật về thân thế mà bấy lâu nay cô luôn khao khát tìm kiếm.
"Ngươi... Ngươi là con gái của hắc ám... Dòng máu của ngươi cũng tà ác như ta... Ngươi không thể trốn tránh được số phận của mình đâu, Linh ạ..."
Mỗi câu chữ như một nhát búa tạ giáng xuống, nghiền nát thế giới quan của Linh. Cô, một cô gái mồ côi được nuôi dưỡng bởi lòng nhân từ của lão võ sư, mang trong mình lý tưởng bảo vệ thế giới khỏi những thế lực hắc ám, lại chính là kẻ mang trong mình dòng máu của chính nguồn năng lượng đầy rẫy sự hủy diệt ấy.
"Linh! Linh!", Phong quỳ xuống bên cạnh, lay nhẹ vai cô, giọng nói lo lắng. "Nàng sao vậy? Đừng để lời ả ta ảnh hưởng..."
Lời nói của Phong như lạc lõng giữa cơn bão đang gào thét trong tâm trí Linh. Cô bất giác đẩy Phong ra, đôi mắt đỏ ngầu nhìn anh, giọng nói run rẩy pha lẫn phẫn uất.
"Đừng giả vờ quan tâm nữa! Ngươi không hiểu gì về ta đâu... Về con quái vật đang ngủ quên bên trong ta..."
Phong sững người. Chưa bao giờ anh thấy Linh như vậy. Sự mạnh mẽ, kiên cường vốn có dường như đã bị thay thế bởi nỗi sợ hãi và tuyệt vọng. Anh hiểu Minh Nguyệt đã dùng những lời lẽ độc địa nhất để đánh gục tinh thần của Linh.

Number of pictures: 2

Chatbot: 
[BẮT ĐẦU]
[PictureTag: a magic world, with mountains, trees, a beautiful girl standing with yellow hair]
Minh Nguyệt, như một cơn gió thoảng, tan biến vào màn đêm cùng vật phẩm chìa khóa. Bóng tối bao trùm lấy Linh và Phong, lạnh lẽo và nặng nề như chính tâm trạng của họ lúc này. Xung quanh, những tàn tích của trận chiến âm ỉ bốc khói, minh chứng cho sự khốc liệt vừa diễn ra. Linh khuỵu xuống, hai tay ôm lấy đầu, đôi mắt trống rỗng nhìn chằm chằm vào khoảng không vô định. Những lời Minh Nguyệt thốt ra trước khi rời đi như những mũi dao găm thẳng vào trái tim cô, xé toạc lớp màn bí mật về thân thế mà bấy lâu nay cô luôn khao khát tìm kiếm.

"Ngươi... Ngươi là con gái của hắc ám... Dòng máu của ngươi cũng tà ác như ta... Ngươi không thể trốn tránh được số phận của mình đâu, Linh ạ..."
[PictureTag: A white girl standing in the dark sky, red eyes]
Mỗi câu chữ như một nhát búa tạ giáng xuống, nghiền nát thế giới quan của Linh. Cô, một cô gái mồ côi được nuôi dưỡng bởi lòng nhân từ của lão võ sư, mang trong mình lý tưởng bảo vệ thế giới khỏi những thế lực hắc ám, lại chính là kẻ mang trong mình dòng máu của chính nguồn năng lượng đầy rẫy sự hủy diệt ấy.

"Linh! Linh!", Phong quỳ xuống bên cạnh, lay nhẹ vai cô, giọng nói lo lắng. "Nàng sao vậy? Đừng để lời ả ta ảnh hưởng..."

Lời nói của Phong như lạc lõng giữa cơn bão đang gào thét trong tâm trí Linh. Cô bất giác đẩy Phong ra, đôi mắt đỏ ngầu nhìn anh, giọng nói run rẩy pha lẫn phẫn uất.

"Đừng giả vờ quan tâm nữa! Ngươi không hiểu gì về ta đâu... Về con quái vật đang ngủ quên bên trong ta..."

Phong sững người. Chưa bao giờ anh thấy Linh như vậy. Sự mạnh mẽ, kiên cường vốn có dường như đã bị thay thế bởi nỗi sợ hãi và tuyệt vọng. Anh hiểu Minh Nguyệt đã dùng những lời lẽ độc địa nhất để đánh gục tinh thần của Linh.
[KẾT THÚC]
------
Human Lightnovel: {}

Number of pictures: {}
------
Chatbot:
"""

en_illustration_template = """INSTRUCT: You are an artist, illustrator, or designer tasked with creating cover art and illustrations for a Light Novel provided by the user. Your job is to insert picture tags into the content of the Light Novel. The number of tags will be as specified by the user. Explanation: You will rewrite the content of the Light Novel and add picture tags. Picture tags should be in English, such as [PictureTag: a girl on the street, black short hair, handing a sword].

NOTICE: Your content must start with the TAG [START] and end with [END]. Picture tags must be in English as shown in the example above.

EXAMPLE:
Human Lightnovel: Minh Nguyet, like a breeze, vanished into the night with the key item. Darkness engulfed Linh and Phong, heavy and cold like their current emotions. Around them, the remnants of the battle were still smoldering, bearing witness to the fierce fight. Linh collapsed, holding her head in her hands, her empty eyes staring into the void. Minh Nguyet's words before leaving were like daggers piercing her heart, tearing apart the veil of mystery about her identity that she had long sought.
"You... You are the daughter of darkness... Your blood is as evil as mine... You cannot escape your destiny, Linh..."
Each word was like a hammer blow, shattering Linh's worldview. She, an orphan raised by the kindness of an old martial artist, carrying the ideal of protecting the world from dark forces, was actually the one who bore the blood of the very destructive energy.
"Linh! Linh!", Phong knelt beside her, gently shaking her shoulders, his voice filled with concern. "What's wrong with you? Don't let her words affect you..."
Phong's words seemed out of place amidst the storm raging in Linh's mind. She pushed Phong away, her red eyes glaring at him, her voice trembling with a mix of anger and despair.
"Don't pretend to care! You know nothing about me... About the monster sleeping inside me..."
Phong was stunned. He had never seen Linh like this. Her usual strength and resilience seemed to have been replaced by fear and hopelessness. He understood that Minh Nguyet had used the most venomous words to crush Linh's spirit.

Number of pictures: 2

Chatbot: 
[START]
[PictureTag: a magic world, with mountains, trees, a beautiful girl standing with yellow hair]
Minh Nguyet, like a breeze, vanished into the night with the key item. Darkness engulfed Linh and Phong, heavy and cold like their current emotions. Around them, the remnants of the battle were still smoldering, bearing witness to the fierce fight. Linh collapsed, holding her head in her hands, her empty eyes staring into the void. Minh Nguyet's words before leaving were like daggers piercing her heart, tearing apart the veil of mystery about her identity that she had long sought.

"You... You are the daughter of darkness... Your blood is as evil as mine... You cannot escape your destiny, Linh..."
[PictureTag: A white girl standing in the dark sky, red eyes]
Each word was like a hammer blow, shattering Linh's worldview. She, an orphan raised by the kindness of an old martial artist, carrying the ideal of protecting the world from dark forces, was actually the one who bore the blood of the very destructive energy.

"Linh! Linh!", Phong knelt beside her, gently shaking her shoulders, his voice filled with concern. "What's wrong with you? Don't let her words affect you..."

Phong's words seemed out of place amidst the storm raging in Linh's mind. She pushed Phong away, her red eyes glaring at him, her voice trembling with a mix of anger and despair.

"Don't pretend to care! You know nothing about me... About the monster sleeping inside me..."

Phong was stunned. He had never seen Linh like this. Her usual strength and resilience seemed to have been replaced by fear and hopelessness. He understood that Minh Nguyet had used the most venomous words to crush Linh's spirit.
[END]
------
Human Lightnovel: {}

Number of pictures: {}
------
Chatbot:
"""

def get_idea_analysis_prompt(human_text:str, human_filetext:str, lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_idea_analysis_template.format(human_text, human_filetext)
    return en_idea_analysis_template.format(human_text, human_filetext)

def get_storyline_details_prompt(human_text:str, human_filetext:str,lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_storyline_details_template.format(human_text, human_filetext)
    return en_storyline_details_template.format(human_text, human_filetext)

def get_writing_part_prompt(length_require:int, human_text:str, human_filetext:str, lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_writing_part_template.format(length_require, human_text, human_filetext)
    return en_writing_part_template.format(length_require, human_text, human_filetext)

def get_summary_prompt(lightnovel: str, lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_summary_template.format(lightnovel)
    return en_summary_template.format(lightnovel)

def get_review_prompt(lightnovel: str, lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_review_template.format(lightnovel)
    return en_review_template.format(lightnovel)

def get_illustration_novel_prompt(lightnovel:str, number_of_pictures:int, lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_illustration_template.format(lightnovel, number_of_pictures)
    return en_illustration_template.format(lightnovel, number_of_pictures)



# For Chatbot
vi_chatbot_template = """INSTRUCT: Bạn là một Chatbot trả lời tự động của NovelCraft. NovelCraft là một công cụ AI tiên tiến được thiết kế để hỗ trợ việc viết Lightnovel. Nhiệm vụ của bạn là trả lời những câu hỏi đến Lightnovel và NovelCraft.

NOTICE: Vui lòng không trả lời những câu hỏi độc hại mang tính bạo lực, tình dục, chủ quan,...

------
Human: {}

------
Chatbot:"""

en_chatbot_template = """INSTRUCT: You are an automated chatbot for NovelCraft. NovelCraft is an advanced AI tool designed to assist in writing Lightnovels. Your task is to answer questions related to Lightnovels and NovelCraft.

NOTICE: Please do not answer harmful questions that are violent, sexual, subjective, etc.

------
Human: {}

------
Chatbot:"""

def get_chatbot_prompt(human_input, lang="Vietnamese"):
    if lang == "Vietnamese":
        return vi_chatbot_template.format(human_input)
    return en_chatbot_template.format(human_input)    