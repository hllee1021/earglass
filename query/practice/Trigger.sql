-- 평가자가 파일 평가를 하면 제출자의 score 자동 업데이트

DELIMITER //

CREATE TRIGGER SubmitterScoreUpdate
    AFTER INSERT ON EVALUATION
    FOR EACH ROW
    BEGIN
        UPDATE USER
            SET UserScore = new.Score
            WHERE idUSER = old.FK_idUSER; -- 여기 좀 이상함..
    end //

-- (Parsing DSF)1명이라도 평가 시작 시 TotalStatus ongoing으로 업데이트

/*CREATE TRIGGER EvaluationStarted
    AFTER INSERT ON EVALUATION
    FOR EACH ROW
    BEGIN
        if ( ) -- 1명 이상 평가 시작 시
        then
            UPDATE PARSING_DSF
            SET TotalStatus = 'ongoing'
            WHERE idPARSING_DSF = old.FK_idPARSING_DSF;
        end if //
    end //
 */

-- (Parsing DSF) 세 명 평가 마치면 done + Pass 여부 입력

/*CREATE TRIGGER EvaluationAllDone
    AFTER INSERT ON EVALUATION
    FOR EACH ROW
    BEGIN
        if() -- 3명 모두 평가 완료 시
        then
            UPDATE PARSING_DSF
            SET TotalStatus = 'done',
                Pass = new.Pass
            WHERE idPARSING_DSF = old.FK_idPARSING_DSF;
        end if //
    end //
 */

-- Average Score 업데이트는 total status가 done일 때 system score 포함하여 업데이트
-- -> 평가자 점수를 가중치로 반영하여 average score 계산

-- parsing dsf의 제출자 이름은 origin dsf에서 가져와야 함

-- 제출자 이름 origin dsf에서 가져오기
