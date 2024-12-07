##### 1. 랜덤으로 숫자를 생성하려면, 코드 실행 중 의도적으로 지연시간을 주려면 먼저 어떻게 해야할까요? #####

import random #랜덤 숫자 생성 모듈 임포트
import time #지연시간 모듈 임포트

##### 2. 매개변수를 받아서 생성자의 인스턴스 변수를 초기화해보세요! ##########

class Character:
    def __init__(self, name, hair, clothes, shoes):
         self.name=name
         self.hair=hair
         self.clothes=clothes
         self.shoes=shoes

class DetectiveGame:
    def __init__(self):
        self.characters = [
            Character("전환", "장발이야", "운동복을 입었어", "운동화를 신었어"),
            Character("이동현", "파란 모자를 썼어", "양복을 입었어", "구두를 신었어"),
            Character("김정석", "노랑 머리야", "무스탕을 입었어", "아무것도 안 신고 있었어"),
            Character("정준영", "스님 머리야", "셔츠를 입었어", "슬리퍼 신었어"),
            Character("박정은", "단발머리야", "치마를 입었어", "어그를 신었어"),
            Character("김현수", "곱슬머리야", "반팔티를 입었어", "크록스를 신었어"),
            Character("이준기", "허리까지 머리카락이 있어", "아무것도 안 입었어", "양말만 신고있었어")
        ]

        ##### 3. 게임 초기 세팅을 해봅시다. #######################################################
        ##### self.murderer, self.victim, self.suspect는 아직 정해지지 않았습니다.
        ##### self.dying_message, self.detective_name도 마찬가지로 아직 정해지지 않았습니다.
        ##### self.clues도 마찬가지로 아직 정해지지 않았습니다. self.clues는 리스트 자료형을 가집니다.
        ##### self.lives, 즉 기회는 단 2번입니다.
        ##### 주어진 조건을 바탕으로 세팅을 진행하세요!

        self.murderer=None #범인
        self.victim=None #희생자
        self.suspect=None #플레이어가 범인으로 지목한 용의자
        self.dying_message=None #다잉메세지
        self.detective_name=None #플레이어 이름
        self.clues=[] #단서들
        self.lives=2 #정답 기회
        
    def show_intro(self):
        print("탐정 게임에 오신 것을 환영합니다.")
        time.sleep(1)

        ##### 4. 탐정님의 이름을 알려주세요! Python으로 입력을 받아 봅시다. ###########

        self.detective_name=input("탐정님의 이름을 알려주세요!: ")

        ##### 5. 게임의 캐릭터 중 한 명을 랜덤으로 희생자로 지정하고, 희생자로 지정된 캐릭터를 목록에서 제거해주세요! #############

        self.victim=random.choice(self.characters) #희생자 랜덤지정
        self.characters.remove(self.victim) #희생자 캐릭터 제거
        self.murderer = random.choice(self.characters) #범인 랜덤 지정
        dying_message_type = random.choice(["hair", "clothes", "shoes"]) #알려줄 단서 종류 랜덤 지정

        ###### 6. 캐릭터들의 속성 중 하나를 다잉메시지로 출력해주세요. match_dying_message 함수를 참고해서 작성하시면 됩니다. #####
        
        if dying_message_type=="hair":
            self.dying_message= f"머리스타일은 {getattr(self.murderer, dying_message_type)} 윽..☠️"
        elif dying_message_type=="clothes":
            self.dying_message= f"옷은 {getattr(self.murderer, dying_message_type)} 윽..☠️"
        elif dying_message_type=="shoes":
            self.dying_message= f"신발은 {getattr(self.murderer, dying_message_type)} 윽..☠️" 
        

        ######################################################################################################

        print(f"########################################")
        print(f"#######        평화로운 해커톤              ")
        print(f"########################################")
        time.sleep(1.5)


        print(f"\n코딩에 몰두하던 {self.detective_name}, 눈이 피로해지기 시작한다. 해커톤의 열기가 고조될수록, 정신은 점점 흐릿해진다.")
        time.sleep(1)
        print(f"{self.detective_name}: 이 해커톤, 너무 평화롭기만 하군... 뭔가 재밌는 사건이라도 터져야 할 텐데. 뭐, 코드가 몽땅 날아가는 일이라든지.")
        time.sleep(1)
        print(f"{self.victim.name}: 하하, 탐정님! 그런 무서운 말씀은 제발 그만하세요. 상상만 해도 아찔하네요... 그런 일은 절대로 일어나지 않을 거예요.")
        time.sleep(1)
        print(f"{self.detective_name}: 뭐, 그렇긴 하겠지. 아, 참고로 나는 명탐정 {self.detective_name}! 사건이 터지면 언제든 나를 찾아.")
        time.sleep(1)
        print(f"{self.victim.name}: 하하, 명탐정님! 알겠습니다. 그런데 요즘 제 노트북을 자꾸 누가 훔쳐보는 것 같아서 신경 쓰이긴 해요. 집 앞 카페에서 코딩하다 보면 말이죠...")
        time.sleep(1)
        print(f"그렇게 둘은 헤어졌고, 그로부터 10분 후 갑자기 정전이 일어나게 되는데..\n")
        time.sleep(1)

        print(f"########################################")
        print(f"#######        사건 발생             ")
        print(f"########################################")
        time.sleep(1)

        print(f"갑자기 날카로운 비명 소리가 울려 퍼졌다. {self.victim.name}씨의 노트북 화면이 순식간에 블루스크린으로 바뀌었다.")
        time.sleep(1)
        print(f"그 충격에 {self.victim.name}씨는 정신을 잃고 그대로 쓰러졌다...")
        time.sleep(1)

        print(f"\n현장은 순식간에 혼란에 빠졌고, 바닥에는 {self.victim.name}씨의 메시지가 남겨져 있었다.")
        time.sleep(1)

        print("\n================사망하지는 않았지만 이게 다잉메시지?!================")
        print(f"                    \"{self.dying_message}\"")
        print("=================================================================")
        time.sleep(1)

        ###### 7. 용의자 총 인원 수를 어떻게 계산할 수 있을까요?  #########
        
        # 이 줄부터 코드를 작성해주세요!
        print("용의자는 총 %d명..." %(len(self.characters)))
                
        ########################################################
        time.sleep(1)

        print(f"그중, 범인은 바로 이 자리에 있을 것입니다...")
        time.sleep(1)
        print(f"{self.detective_name}님의 임무는 범인을 찾아내는 것입니다. 진실을 밝혀내세요. 기회는 2번입니다.\n")
        time.sleep(1)

        print(f"########################################")
        print(f"#######        추리 시작               ")
        print(f"########################################")
        time.sleep(1)

    def investigate(self):
        print("용의자와 대화를 나누고 인상착의를 수집하세요...\n")
        for index, char in enumerate(self.characters, 1):
            print(f"{index}. {char.name}")

        print("\n누구를 조사하시겠습니까? 이름을 입력하세요: ", end="")
        choice_name = input().strip()

        ##### 8. 사용자가 입력한 이름을 가진 용의자를 조사하려면 어떻게 해야 할까요? 반복문과 if문, 그리고 append 메서드를 활용해보세요! ########

        for i in self.characters:
            if i.name==choice_name:
                print(f"\n================용의자 {i.name}의 정보================")
                print(f"{i.hair}..!")
                print(f"{i.clothes}..!")
                print(f"{i.shoes}..!")
                self.clues.append(f"{i.name}씨는 {i.hair}. {i.clothes}.. {i.shoes}..!")
                return

        #####################################################################################

        print("잘못된 입력입니다! 시간이 얼마 남지 않았습니다, 다시 시도해주세요!")
        print("범인은 아직도 우리 곁에 있어요. 서둘러 진실을 밝혀내야 합니다!")
        print(f"{self.detective_name}: 좋아, 이번엔 잘 선택해보자.\n")

        ##### 9. 다시 잘 선택해보려면 어떤 단계로 돌아가야 할까요? 특정 함수를 재실행해봅시다. #################

        self.investigate()

        #####################################################################################

    def match_dying_message(self, character):
        if self.dying_message == f"머리스타일은 {character.hair} 윽..☠️" or \
                self.dying_message == f"옷은 {character.clothes} 윽..☠️" or \
                self.dying_message == f"신발은 {character.shoes} 윽..☠️":
            return True
        return False

    def prompt_choice(self, prompt):
        while True:
            choice = input(prompt).strip().lower()
            if choice in ['네', '아니오']:
                return choice
            print("잘못된 입력입니다. 네 또는 아니오만 입력해 주세요.")

    def accuse(self):
        print("\n범인을 지목할 시간입니다.")

        ##### 10. self.characters 리스트의 각 항목을 인덱스와 함께 출력하세요. enumerate를 활용해보세요! ##########

        for index, char in enumerate(self.characters, 1):
            print(f"{index}. {char.name}")

        ###########################################################################################

        print("\n누구를 범인으로 지목하시겠습니까? 이름을 입력하세요: ", end="")
        choice_name = input().strip()
        print(f"{self.detective_name}: 범인은 바로 {choice_name}씨야")
        for char in self.characters:
            if char.name == choice_name:
                self.suspect = char
                self.check_outcome()
                return

        print("탐정님, 그건 잘못된 선택입니다! 시간이 얼마 남지 않았습니다, 다시 시도해주세요!")
        print("범인은 아직도 우리 곁에 있어요. 서둘러 진실을 밝혀내야 합니다!")
        print(f"{self.detective_name}: 좋아, 이번엔 잘 선택해보자.\n")
        time.sleep(1)
        self.accuse()


    def check_outcome(self):
        if self.match_dying_message(self.suspect):
            print("""
----------------------------------------------------------------------------------


     ██████╗  █████╗ ███╗   ███╗███████╗    ██╗    ██╗██╗███╗   ██╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║    ██║██║████╗  ██║
    ██║  ███╗███████║██╔████╔██║█████╗      ██║ █╗ ██║██║██╔██╗ ██║
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║███╗██║██║██║╚██╗██║
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚███╔███╔╝██║██║ ╚████║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝


----------------------------------------------------------------------------------""")
            time.sleep(1)
            print(f"###############################################")
            print(f"#######        당신은 역시 명탐정!!         ")
            print(f"###############################################")
            time.sleep(1)
            print(f"\n정답입니다! 범인은 바로 {self.suspect.name}씨였습니다!")
            time.sleep(1)
            print(f"당신의 추리는 완벽했습니다, 역시 명탐정 {self.detective_name} 답군요.")
            time.sleep(1)
            print(f"\n{self.detective_name}: 왜 노트북을 망가뜨렸습니까?? {self.victim.name}씨의 노트북을 왜 그렇게 했죠?")
            time.sleep(1)
            print(f"{self.suspect.name}: 그게 사실... {self.victim.name}씨의 팀이 해커톤 우승을 못하게 하려고... 그래서 홧김에.. 죄송합니다🥹")
            time.sleep(1)
            print(f"\n{self.suspect.name}씨는 끝내 자신의 범행을 인정했고, 피로그래밍 22기 해커톤에서 퇴출당했습니다.")
            time.sleep(1)
            print(f"사건은 해결되었고, 모든 사람들이 안도의 한숨을 내쉬었습니다. 당신의 활약 덕분입니다.")
            time.sleep(1)
            self.ask_restart()

        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"\n{self.suspect.name}: 무슨 소리야? 내 인상착의를 봐... 당신 명탐정 맞아? 💢💢💢")
                print(f"\n틀렸습니다... {self.suspect.name}씨는 범인이 아닙니다. 남은 기회는 {self.lives}번입니다.")
                print(f"시간이 얼마 남지 않았어요. 신중하게 선택해주세요.")
                time.sleep(1)
                choice = self.prompt_choice("용의자들의 인상착의를 다시 보겠습니까? (네/아니오): ")
                if choice == '네':
                    print(f"{self.detective_name}: 좋았어... 다시 차근차근 보자\n")
                    time.sleep(1)
                    self.main_flow()  
                else:
                    self.accuse()  # 다시 지목할 기회를 줌
            else:
                print(
                    """
----------------------------------------------------------------------------------


    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


----------------------------------------------------------------------------------"""
                )
                time.sleep(1)
                print(f"########################################")
                print(f"#######         추리 실패......           ")
                print(f"########################################")
                time.sleep(1)
                print(f"\n{self.murderer.name}: 명탐정 별거 없네~~~ 해커톤 우승은 내꺼다!!!")
                time.sleep(1)
                print(f"\n안타깝습니다... 범인은 {self.murderer.name}씨였습니다. 모든 기회를 다 써버렸습니다.")
                time.sleep(1)
                print(f"추리는 실패했습니다. {self.detective_name} 탐정님, 이번 사건은 당신에게 큰 상처로 남게 될 것입니다.")
                time.sleep(1)
                print(f"당신은 이 미스터리를 풀 기회를 잃었습니다...")
                time.sleep(1)
                print(f"하지만, 진정한 탐정은 실패에서도 배웁니다. 다음엔 꼭 진실을 밝혀내세요.")
                time.sleep(1)
                self.ask_restart()

    # 게임을 다시 할 건지 물어보는 함수
    def ask_restart(self):
        choice = self.prompt_choice("게임을 다시 시작하시겠습니까? (네/아니오): ")
        if choice == '네':
            self.reset_game()
            self.play()
        else:
            print("게임을 종료합니다. 감사합니다!")

    # 게임 재시작 함수
    def reset_game(self):
        
        self.lives = 2
        self.victim = None
        self.murderer = None
        self.clues = []
        self.suspect = None

    # 범인 잡기 실패 후 다시 인상착의 수집
    def main_flow(self):
        # 조사 단계 (인상착의를 수집, 무제한)
        while True:
            self.investigate()
            if self.prompt_choice("\n계속 조사하시겠습니까? (네/아니오): ") == '아니오':
                break

        # 범인 지목
        self.accuse()

    # 게임 플레이!
    def play(self):
        self.show_intro()

        # 조사 단계 (인상착의를 수집, 무제한)
        while True:
            self.investigate()
            if self.prompt_choice("\n계속 조사하시겠습니까? (네/아니오): ") == '아니오':
                break

        # 범인 지목 (목숨 2개)
        self.accuse()


# 게임 실행
if __name__ == "__main__":
    game = DetectiveGame()
    game.play()