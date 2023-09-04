\version "2.24.2"
\language "english"
\context
{
    #(set-global-staff-size 14)

}
% OPEN_BRACKETS:
\context Score = "Score"
<<
    % OPEN_BRACKETS:
    \context Staff = "Exercise_Staff"
    {
        % OPEN_BRACKETS:
        \context Voice = "Exercise_Voice"
        {
            % OPEN_BRACKETS:
            {
                % BEFORE:
                % COMMANDS:
                \repeat volta 2
                % OPEN_BRACKETS:
                {
                    a'4
                    b'4
                    cs''4
                    b'4
                % CLOSE_BRACKETS:
                }
                a'1
                % AFTER:
                % COMMANDS:
                \bar "|."
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    }
% CLOSE_BRACKETS:
>>
