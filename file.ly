\version "2.24.2"
\language "english"
#(set-global-staff-size 14)

    \header {
        composer = \markup { Josquin }
        subtitle = \markup { Agnus dei }
        title = \markup { Missa sexti toni }
    }

    \layout {
        indent = 0
    }
% OPEN_BRACKETS:
\context Score = "Score"
<<
    % OPEN_BRACKETS:
    \context Staff = "Violin_Staff"
    {
        % OPEN_BRACKETS:
        \context Voice = "Violin_Voice"
        {
            c'4
            d'4
            e'4
            f'4
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    }
% CLOSE_BRACKETS:
>>
