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
                % OPENING:
                % COMMANDS:
                \time 3/4
                a'2.
                % AFTER:
                % SPANNER_STARTS:
                ~
                a'2.
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
